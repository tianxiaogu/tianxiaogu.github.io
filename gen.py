#! /usr/bin/python

import os, sys, traceback

from jinja2 import Template
import markdown
from markdown.inlinepatterns import Pattern
from markdown.util import etree, AtomicString

import fencedcode

DIR=os.path.dirname(os.path.abspath(__file__))

#---------------------------



#---------------------------
def create_markdown():
    md = markdown.Markdown(extensions = [
            'markdown.extensions.extra',
            'markdown.extensions.meta',
            'markdown.extensions.admonition',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            fencedcode.makeExtension()],
            extension_configs= {
                'markdown.extensions.codehilite' : {
                        'linenums' : True
                    }
                })

    return md

#------------------------

class Page(object):
    pass

def get_markdown_page(page_path):
    page = Page()
    with open(page_path, 'r') as f:
        md = create_markdown()
        page.html = md.convert(f.read().decode('utf-8'))
        page.meta = md.Meta # flask-pages naming convention
        for key, value in page.meta.iteritems():
            page.meta[key] = ''.join(value) # meta is a list

        return page

def gen():
    with open('template.html') as f:
        template = Template(f.read().decode('utf-8'))
    with open('redirect.html') as f:
        t_redirect = Template(f.read().decode('utf-8'))

    for root, dirs, files in os.walk(DIR):
        for f in files:
            if f.endswith('.md'):
                mdpath = os.path.join(root, f)
                page = get_markdown_page(mdpath)
                with open(mdpath[:-2] + 'html', 'w') as htmlpath:
                    htmlpath.write(template.render(page = page).encode('utf-8'))
                if f != 'index.md':
                    # compatible with moon
                    folder = mdpath[:-3]
                    if os.path.exists(folder) and os.path.isdir(folder):
                        pass
                    else:
                        os.makedirs(folder)

                    target = '/' + os.path.relpath(root, DIR).replace('\\', '/') + '/' + f[:-2] + 'html'
                    with open(os.path.join(folder, 'index.html'), 'w') as rd:
                        rd.write(t_redirect.render(target = target).encode('utf-8'))




if __name__ == '__main__':
    try:
        gen()
    except:
        traceback.print_exc()
