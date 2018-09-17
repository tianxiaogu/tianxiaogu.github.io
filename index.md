title: Homepage

# Tianxiao Gu 顾天晓


----------------

* Postdoc
* Department of Computer Science
* University of California, Davis, USA
* Supervisor: Prof. [Zhendong Su](http://www.cs.ucdavis.edu/~su/)
* Email: tianxiao.gu (at) gmail dot com
* <a href="http://www.linkedin.com/in/tianxiaogu"><i class="fab fa-linkedin-square"></i></a>
  <a href="https://twitter.com/Xiaotiangu"><i class="fab fa-twitter-square"></i></a>
  <a href="https://www.facebook.com/eric.ku.505"><i class="fab fa-facebook-square"></i></a>
  <a href="https://www.bitbucket.org/txgu/"><i class="fab fa-bitbucket"></i></a>
  <a href="https://github.com/tianxiaogu"><i class="fab fa-github"></i></a>



----------------
## Research Interests

* Fuzz Testing
* [Compiler Testing](./testing/compiler/)
    * `pytkfuzz`: A python implementation of [`tkfuzz`](https://chengniansun.bitbucket.io/papers/issta16.pdf).
* Java Virtual Machine
    * [Bytecode generator](./testing/jvm/)
        * [Reported bugs](./testing/jvm/)
* Android Application Testing
    * [Ape](./sata): A framework for model-based testing for Android apps.
        * Crashes detected by Ape using only 15 minitues: [list1](https://ape-report.github.io/)[list2](https://ape-report.github.io/ape-report-1).
        * [Reported bugs](./sata/reported-bugs) found by Ape using only half an hour.
    * WGDroid: A fancy GUI exploration tool developed on top of Ape.
    * [AimDroid](https://icsnju.github.io/AimDroid-ICSME-2017/)
    * MiniTracing: Collect method/coverage without bytecode instrumentation.
        * [Android 6 (binary for x86)](art-mt-x86.zip): Android ART with method/instruction coverage support.
        * [Android 4.4 (binary for x86)](dalvikvm-mt-x86.zip): Android Dalvik VM with method/instruction coverage support.
        * [android-mt-cmd](https://bitbucket.org/txgu/android-mt-cmd): Command line tools to collect coverage.
        * [android-mt-parser](https://bitbucket.org/txgu/android-mt-parser): Parser for the coverage data.
* Dynamic Software Updating
    * A [list](./javelus/literature) of practical DSU tools.
* Program Analysis
* Programming Languages

----------------

## Education and Work Experience

* 2017.5 - : Postdoc, University of California, Davis.
* 2010.9 - 2017.3: Ph.D., Department of Computer Science and Technology, Nanjing University, supervised by Prof. [Xiaoxing Ma](http://moon.nju.edu.cn/people/xiaoxingma "Xiaoxing Ma")
* 2015.6 - 2015.7: Intern at the JVM Optimization Group in [Ant Financial](http://www.antgroup.com) (formerly known as [Alipay](https://www.alipay.com))
* 2013.9 - 2014.9: Visiting Student, University of California, Davis, Prof. [Zhendong Su](http://www.cs.ucdavis.edu/~su/).
* 2006.9 - 2010.6: B.S., Department of Computer Science and Technology, Nanjing University

----------------
## Publications

~~~{.bibtexhtml hl_lines="Tianxiao Gu"}
@inproceedings{gu_automating_2018,
  author    = {Tianxiao Gu and Xiaoxing Ma and Chang Xu and Yanyan Jiang and Chun Cao and Jian Lu},
  title     = {Automating Object Transformations for Dynamic Software Updating via Online Execution Synthesis},
  pages     = {to appear},
  year      = {2018},
  booktitle = {Proceedings of the 32nd European Conference on Object-Oriented Programming (ECOOP 2018)},
}
@inproceedings{wang_aatt_2018,
  author  = {Jue Wang and Yanyan Jiang and Chang Xu and Qiwei Li and Tianxiao Gu and Jun Ma and Xiaoxing Ma and Jian Lu},
  title   = {AATT+: Effectively Manifesting Concurrency Bugs in Android Apps},
  journal = {Science of Computer Programming (SCP)},
  year    = {2018},
  volume  = {0},
  number  = {0},
  pages   = {to appear},
}
@inproceedings{sun_perses_2018,
  title = {Perses: Syntax-Guided Program Reduction},
  author = {Chengnian Sun and Yuanbo Li and Qirun Zhang and Tianxiao Gu and Zhendong Su},
  booktitle = {Proceedings of the 40th International Conference on Software Engineering (ICSE 2018)},
  year = {2018},
  pages = {To appear},
}
@inproceedings{gu_AimDroid:_2017,
  title = {AimDroid: Activity-Insulated Multi-level Automated Testing for Android Applications},
  author = {Tianxiao Gu and Chun Cao and Tianchi Liu and Chengnian Sun and Jing Deng and Xiaoxing Ma and Jian L{\"u}},
  booktitle = {Proceedings of the 2017 IEEE International Conference on Software Maintenance and Evolution (ICSME 2017)},
  year = {2017},
  pages = {103--114},
}
@inproceedings{gu_synthesize_2017,
  author    = {Tianxiao Gu and Xiaoxing Ma and Chang Xu and Yanyan Jiang and Chun Cao and Jian L{\"u}},
  title     = {Synthesizing Object Transformation for Dynamic Software Updating},
  booktitle = {Proceedings of the 39th International Conference on Software Engineering Companion (ICSE-C 2017)},
  pages     = {336--338},
  year      = {2017},
}
@inproceedings{gu_precise_2016,
  author    = {Tianxiao Gu and Ruiqi Liu and Xiaoxing Ma and Zelin Zhao},
  title     = {Precise Heap Differentiating Using Access Path and Execution Index},
  booktitle = {Proceedings of the 15th National Software Application Conference (NASAC 2016)},
  pages     = {133--148},
  year      = {2016},
  url       = {http://dx.doi.org/10.1007/978-981-10-3482-4_10},
}
@inproceedings{li_effectively_2016,
  author    = {Qiwei Li and Yanyan Jiang and Tianxiao Gu and Chang Xu and Jun Ma and Xiaoxing Ma and Jian L{\"u}},
  title     = {Effectively Manifesting Concurrency Bugs in Android Apps},
  booktitle = {Proceedings of the 23rd Asia-Pacific Software Engineering Conference (APSEC 2016)},
  pages     = {209--216},
  year      = {2016},
  url       = {https://doi.org/10.1109/APSEC.2016.038},
}
@inproceedings{gu_improving_2016,
  author    = {Tianxiao Gu and Zelin Zhao and Xiaoxing Ma and Chang Xu and Chun Cao and Jian L{\"u}},
  title     = {Improving Reliability of Dynamic Software Updating Using Runtime Recovery},
  booktitle = {Proceedings of the 23rd Asia-Pacific Software Engineering Conference (APSEC 2016)},
  pages     = {257--264},
  year      = {2016},
  url       = {https://doi.org/10.1109/APSEC.2016.044},
}
@inproceedings{zhao_cure_2016,
  author    = {Zelin Zhao and Tianxiao Gu and Xiaoxing Ma and Chang Xu and Jian L{\"u}},
  title     = {CURE: Automated Patch Generation for Dynamic Software Update},
  booktitle = {Proceedings of the 23rd Asia-Pacific Software Engineering Conference (APSEC 2016)},
  pages     = {249--256},
  year      = {2016},
  url       = {https://doi.org/10.1109/APSEC.2016.043},
}
@inproceedings{gu_automatic_2016,
  author    = {Tianxiao Gu and Chengnian Sun and Xiaoxing Ma and Jian L{\"u} and Zhendong Su},
  title     = {Automatic Runtime Recovery via Error Handler Synthesis},
  booktitle = {Proceedings of the 31st IEEE/ACM International Conference on Automated Software Engineering (ASE 2016)},
  pages     = {684--695},
  year      = {2016},
  url       = {https://doi.org/10.1145/2970276.2970360},
}
@article{gu_low-disruptive_2014,
  author    = {Tianxiao Gu and Chun Cao and Chang Xu and Xiaoxing Ma and Linghao Zhang and Jian L{\"u}},
  title     = {Low-disruptive Dynamic Updating of Java Applications},
  journal   = {Information & Software Technology},
  volume    = {56},
  number    = {9},
  pages     = {1086--1098},
  year      = {2014},
  url       = {https://doi.org/10.1016/j.infsof.2014.04.003},
}
@inproceedings{jiang_care:_2014,
  author    = {Yanyan Jiang and Tianxiao Gu and Chang Xu and Xiaoxing Ma and Jian L{\"u}},
  title     = {CARE: Cache Guided Deterministic Replay for Concurrent Java Programs},
  booktitle = {Proceedings of the 36th International Conference on Software Engineering (ICSE 2014)},
  pages     = {457--467},
  year      = {2014},
  url       = {https://doi.org/10.1145/2568225.2568236},
}
@inproceedings{zhang_resynchronizing_2012,
  author    = {Linghao Zhang and Chang Xu and Xiaoxing Ma and Tianxiao Gu and Xuezhi Hong and Chun Cao and Jian L{\"u}},
  title     = {Resynchronizing Model-Based Self-Adaptive Systems with Environments},
  booktitle = {Proceedings of the 19th Asia-Pacific Software Engineering Conference (APSEC 2012)},
  pages     = {184--193},
  year      = {2012},
  url       = {https://doi.org/10.1109/APSEC.2012.62},
}
@inproceedings{gu_javelus_2012,
  author    = {Tianxiao Gu and Chun Cao and Chang Xu and Xiaoxing Ma and Linghao Zhang and Jian L{\"u}},
  title     = {Javelus: A Low Disruptive Approach to Dynamic Software Updates},
  booktitle = {Proceedings of the 19th Asia-Pacific Software Engineering Conference (APSEC 2012)},
  pages     = {527--536},
  year      = {2012},
  url       = {https://doi.org/10.1109/APSEC.2012.55},
}

~~~

----------------
## Projects


!!! note
    A project may not be publicly available if we are working on a paper about it.

* <a href="https://bitbucket.org/txgu/javelus"><i class="fab fa-bitbucket"></i></a> [Javelus](./javelus/): Low-disruptive Dynamic Updating of Java Applications.
    * A dynamic-updating-enabled JVM built on top the HotSpot JVM in OpenJDK 8
* <a href="https://bitbucket.org/txgu/javelus"><i class="fab fa-bitbucket"></i></a> [MiniTracing](./minitracing/)
    * A whole program tracing tool that can trace method entrance/exit, object allocation, GC moving, and locking/unlocking events in the JVM.
    * Checkout the branch `mini-tracing` of `javelus`
    * Other tools based on this project:
        * [PHD](https://bitbucket.org/txgu/phd): Precise Heap Differentiating: An experimental tool aiming at precisely differentiating two heap snapshots.
* <a href="https://bitbucket.org/txgu/ares"><i class="fab fa-bitbucket"></i></a> [Ares](./ares/): Automatic Runtime Recovery via Error Handler Synthesis.
* <a href="https://bitbucket.org/txgu/aotes-asm"><i class="fab fa-bitbucket"></i></a> AOTES: Automating Object Transformations for Dynamic Software Updating via Execution Synthesis 
* <a href="https://bitbucket.org/txgu/sata"><i class="fab fa-bitbucket"></i></a> [Ape](./sata/): Automated Testing of Android Applications with Abstraction Refinement.


--------------------

## Awards


* Supported by the Program B for Outstanding PhD candidate of Nanjing University, 2015
* Tung OOCL Scholarship, Nanjing University, 2014
* Outstanding Graduate Student Scholarship, Nanjing University, 2012
* People Scholarship, Second Prize, Nanjing University, 2009
* First Provincial-level in Mathematical Contest in Modeling for College Students, 2008
* People Scholarship, Third Prize, Nanjing University, 2008
* People Scholarship, Third Prize, Nanjing University, 2007




