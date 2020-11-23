#! /usr/bin/env python2
from __future__ import absolute_import
from __future__ import unicode_literals
import os, sys, traceback

from jinja2 import Environment, FileSystemLoader
import markdown
from markdown.inlinepatterns import Pattern
from markdown.util import etree, AtomicString
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
from markdown.extensions.codehilite import CodeHilite, CodeHiliteExtension, parse_hl_lines


import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode


import re

from itertools import groupby


DIR=os.path.dirname(os.path.abspath(__file__))

#--------------------------

ENV=Environment(loader=FileSystemLoader(DIR))

bibtex_tpl = ENV.get_template('bibtex.html')
main_tpl = ENV.get_template('template.html')
redirect_tpl = ENV.get_template('redirect.html')


#---------------------------
# Install filters and globals
#---------------------------
class Bundle(object):
    pass

class G(object):

    def __init__(self):
        self.bundle = Bundle()
        self.bundle.code = []

g = G()
ENV.globals.update(g=g)

#--------------------------
# Simulation new page
#--------------------------
def start_new_page():
    global g
    g = G()
    ENV.globals.update(g=g)

#---------------------------
# jstrick
#---------------------------


def make_customjs(code):
    g.bundle.code.append(code)
    return ''

#---------------------------
# Markdown
#---------------------------

"""Copied from FencedCodeExtension
"""
class MoonFencedCodeExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        """ Add MoonFencedBlockPreprocessor to the Markdown instance. """
        md.registerExtension(self)

        md.preprocessors.register(
                                 MoonFencedBlockPreprocessor(md), 'moon_fenced_code_block',
                                 26)


class MoonFencedBlockPreprocessor(Preprocessor):
    FENCED_BLOCK_RE = re.compile(r'''
(?P<fence>^(?:~{3,}|`{3,}))[ ]*         # Opening ``` or ~~~
(\{?\.?(?P<lang>[a-zA-Z0-9_+-]*))?[ ]*  # Optional {, and lang
# Optional highlight lines, single- or double-quote-delimited
(hl_lines=(?P<quot>"|')(?P<hl_lines>.*?)(?P=quot))?[ ]*
}?[ ]*\n                                # Optional closing }
(?P<code>.*?)(?<=\n)
(?P=fence)[ ]*$''', re.MULTILINE | re.DOTALL | re.VERBOSE)
    CODE_WRAP = '<pre><code%s>%s</code></pre>'
    LANG_TAG = ' class="%s"'

    def __init__(self, md):
        super(MoonFencedBlockPreprocessor, self).__init__(md)

        self.checked_for_codehilite = False
        self.codehilite_conf = {}

    def run(self, lines):
        """ Match and store Fenced Code Blocks in the HtmlStash. """

        # Check for code hilite extension
        if not self.checked_for_codehilite:
            for ext in self.md.registeredExtensions:
                if isinstance(ext, CodeHiliteExtension):
                    self.codehilite_conf = ext.config
                    break

            self.checked_for_codehilite = True

        text = "\n".join(lines)
        while 1:
            m = self.FENCED_BLOCK_RE.search(text)
            if m:
                lang = ''
                if m.group('lang'):
                    lang = self.LANG_TAG % m.group('lang')

                # If config is not empty, then the codehighlite extension
                # is enabled, so we call it to highlight the code
                if m.group('lang') == 'bibtexhtml':
                    code = self.parse_bibtex(m.group('code'), m.group('hl_lines'));
                elif m.group('lang') == 'customjs':
                    code = self.parse_customjs(m.group('code'));
                elif self.codehilite_conf:
                    highliter = CodeHilite(m.group('code'),
                            linenums=self.codehilite_conf['linenums'][0],
                            guess_lang=self.codehilite_conf['guess_lang'][0],
                            css_class=self.codehilite_conf['css_class'][0],
                            style=self.codehilite_conf['pygments_style'][0],
                            lang=(m.group('lang') or None),
                            noclasses=self.codehilite_conf['noclasses'][0],
                            hl_lines=parse_hl_lines(m.group('hl_lines')))

                    code = highliter.hilite()
                else:
                    code = self.CODE_WRAP % (lang, self._escape(m.group('code')))

                placeholder = self.md.htmlStash.store(code)
                text = '%s\n%s\n%s'% (text[:m.start()], placeholder, text[m.end():])
            else:
                break
        return text.split("\n")

    def _escape(self, txt):
        """ basic html escaping """
        txt = txt.replace('&', '&amp;')
        txt = txt.replace('<', '&lt;')
        txt = txt.replace('>', '&gt;')
        txt = txt.replace('"', '&quot;')
        return txt

    def parse_bibtex(self, bibtex, hl=None):
        return convert_bibtex(bibtex, hl)

    def parse_customjs(self, code):
        return make_customjs(code)


def makeFencedcodeExtension(**kwargs):
    return MoonFencedCodeExtension(**kwargs)

def create_markdown():
    md = markdown.Markdown(extensions = [
            'markdown.extensions.extra',
            'markdown.extensions.meta',
            'markdown.extensions.admonition',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            makeFencedcodeExtension()],
            extension_configs= {
                'markdown.extensions.codehilite' : {
                        'linenums' : True
                    }
                })

    makeJinjaExpressionPattern(md)
    return md

#------------------------
# Jinja2 Markdown

JINJA_EXPRESSION_RE = r'({{.+?(?<!})}})'

class JinjaExpressionPattern(Pattern):

    def __init__(self, pattern, md):
        Pattern.__init__(self, pattern, md)

    def handleMatch(self, m):
        jinja_block = m.group(2)

        try:
            # render returns a unicode object
            # html = render_template_string(m.group(2))
            html = ENV.from_string(m.group(2)).render()
            place_holder = self.md.htmlStash.store(html)
            return place_holder
        except Exception as e:
            traceback.print_exc()

            el = etree.Element('em')
            el.text = AtomicString('Error %s in rendering %s' % (e, m.group(2)))
            return el




def makeJinjaExpressionPattern(md):
    pass
    md.inlinePatterns.register(JinjaExpressionPattern(JINJA_EXPRESSION_RE, md), 'jinja expression pattern', 189) # after backtick

#------------------------
# Bibtex
#------------------------

def getyear(e):
    return e.get('year', 'Unknown')



def decorate_author(author):
    ''' Simply normalize all FamilyName, GivenName [MiddleName] to GivenName [MiddleName] FamilyName
    '''

    authors = author.split('and')

    new_authors = []
    for a in authors:
        ns = a.strip().split(',')
        if len(ns) == 2:
            new_authors.append(ns[1].strip() + ' ' + ns[0].strip())
        elif len(ns) == 1:
            new_authors.append(ns[0])
        else:
            # should not happen
            new_authors.append(a.strip())

    # if you modify here, you should modify your template
    #return ' and '.join(new_authors)
    return new_authors


# TODO use bibtexparser library customizations
# see https://bibtexparser.readthedocs.org/en/latest/tutorial.html#parsing-the-file-into-a-bibliographic-database-object

HYPEN_HYPEN = u'\u2013' # -- in LaTeX
PAGES_RE = re.compile(r'(?P<begin>[0-9]+)-+(?P<end>[0-9]+)')

def decorate_pages(pages):
    m = PAGES_RE.match(pages)
    if m:
        return m.group('begin') + HYPEN_HYPEN + m.group('end')

    # if not match return
    return pages


def decorate_entries(entries):
    for entry in entries:
        if 'author' in entry:
            entry['author'] = decorate_author(entry['author'])

        if 'pages' in entry:
            entry['pages'] = decorate_pages(entry['pages'])

    return entries

def parse_bibtex(bibtex):
    parser = BibTexParser()
    parser.customization = convert_to_unicode
    try:
        bib_database = bibtexparser.loads(bibtex, parser=parser)
    except Exception as e:
        return bibtex

    entries = decorate_entries(bib_database.entries)
    return entries

def convert_bibtex(bibtex, hl=None):
    entries = parse_bibtex(bibtex)
    return convert_bibentries_to_html(entries, hl)

def convert_bibentries_to_html(entries, hl=''):
    ''' Convert a list of bibtex entries into html

    Args: the list of entries
    '''
    return bibtex_tpl.module.render_entries(entries, hl)


def render_bib_entry(entry, hl=''):
    return bibtex_tpl.module.render_entry(entry, hl).replace('\n', '')


def render_bib_entries(entries, hl='', group_by_year=False):
    if group_by_year:
        entries = sorted(entries, key=getyear, reverse=True)
        conferences = filter(lambda e: e['ENTRYTYPE'] in ['inproceedings','proceedings'], entries)
        journals = filter(lambda e: e['ENTRYTYPE'] in ['article'], entries)

        conf_years = sorted(set([getyear(e) for e in conferences]), reverse=True)
        jour_years = sorted(set([getyear(e) for e in journals]), reverse=True)

        grouped_conf = groupby(conferences, getyear)
        grouped_jour = groupby(journals, getyear)
        try:
            return bibtex_tpl.module.render_entries_group_by_year(conf_years, grouped_conf, jour_years, grouped_jour, hl)
        except Exception as e:
            print(e)

    return bibtex_tpl.module.render_entries(entries, hl)



class Citations(object):

    def __init__(self, bibfile):
        with open(bibfile) as f:
            bibtex_str = f.read()

        self.entries = parse_bibtex(bibtex_str)


    def __getitem__(self, key):
        try:
            return next(e for e in self.entries if e.get('ID') == key or e.get('id') == key)
        except:
            raise KeyError(key)

    def render_entry(self, key, hl=''):
        entry = self.__getitem__(key)

        if not entry:
            return "No such entry with key " + key

        return render_bib_entry(entry, hl)

    def render_entries(self, keys, hl='', group_by_year=False):
        entries = filter(lambda e: e.get('ID') in keys or e.get('id') in keys, self.entries)
        return render_bib_entries(entries, hl)


    def render_all(self, hl='', group_by_year=False):
        return render_bib_entries(self.entries, hl, group_by_year)




#------------------------
# Page
#------------------------

class Page(object):
    pass

def get_markdown_page(page_path):
    page = Page()
    with open(page_path, 'r') as f:
        md = create_markdown()
        start_new_page()
        page.html = md.convert(f.read())
        page.meta = md.Meta # flask-pages naming convention
        for key, value in page.meta.items():
            page.meta[key] = ''.join(value) # meta is a list

        return page

def gen():
    for root, dirs, files in os.walk(DIR):
        for f in files:
            if f.endswith('.md'):
                mdpath = os.path.join(root, f)
                page = get_markdown_page(mdpath)
                with open(mdpath[:-2] + 'html', 'w') as htmlpath:
                    htmlpath.write(main_tpl.render(page = page))
                if f != 'index.md':
                    # compatible with moon
                    folder = mdpath[:-3]
                    if os.path.exists(folder) and os.path.isdir(folder):
                        pass
                    else:
                        os.makedirs(folder)

                    target = '/' + os.path.relpath(root, DIR).replace('\\', '/') + '/' + f[:-2] + 'html'
                    with open(os.path.join(folder, 'index.html'), 'w') as rd:
                        rd.write(redirect_tpl.render(target = target))




if __name__ == '__main__':
    try:
        gen()
    except:
        traceback.print_exc()
