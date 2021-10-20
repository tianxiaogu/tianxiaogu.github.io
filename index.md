title: Homepage

# Tianxiao Gu 顾天晓


----------------

* Senior JVM Engineer,  Alibaba Group, Sunnyvale, CA.
* Email: tianxiao.gu (at) gmail dot com
* <a href="http://www.linkedin.com/in/tianxiaogu"><i class="fab fa-linkedin-square"></i></a>
  <a href="https://twitter.com/Xiaotiangu"><i class="fab fa-twitter-square"></i></a>
  <a href="https://www.facebook.com/eric.ku.505"><i class="fab fa-facebook-square"></i></a>
  <a href="https://www.bitbucket.org/txgu/"><i class="fab fa-bitbucket"></i></a>
  <a href="https://github.com/tianxiaogu"><i class="fab fa-github"></i></a>


----------------

## Education and Work Experience

* 2019.4 - present: Senior Engineer, Alibaba Group, Sunnyvale, CA, USA.
* 2017.5 - 2019.3: Postdoc, University of California, Davis.
* 2010.9 - 2017.3: Ph.D., Department of Computer Science and Technology, Nanjing University, supervised by Prof. [Xiaoxing Ma](http://moon.nju.edu.cn/people/xiaoxingma "Xiaoxing Ma")
* 2015.6 - 2015.7: Intern at the JVM Optimization Group in [Ant Financial](http://www.antgroup.com)
* 2013.9 - 2014.9: Visiting Student, University of California, Davis, Prof. [Zhendong Su](http://www.cs.ucdavis.edu/~su/).
* 2006.9 - 2010.6: B.S., Department of Computer Science and Technology, Nanjing University

----------------
## Selected Publications

~~~{.bibtexhtml hl_lines="Tianxiao Gu"}
@inproceedings{yifei_towards_2021,
  author    = {Yifei Zhang and Tianxiao Gu and Xiaolin Zheng and Lei Yu and Wei Kuai and Sanhong Li},
  title     = {Towards a Serverless Java Runtime},
  pages     = {to appear},
  year      = {2021},
  booktitle = {Proceedings of the 36th IEEE/ACM International Conference on Automated Software Engineering, Industry Showcase (ASE Industry Showcase 2021)},
}
@inproceedings{litong_JPDHeap_2021,
  author    = {Litong You and Tianxiao Gu and Shengan Zheng and Jianmei Guo and Sanhong Li and Yuting Chen, and Linpeng Huang},
  title     = {JPDHeap: A JVM Heap Design for PM-DRAM Memories},
  pages     = {to appear},
  year      = {2021},
  booktitle = {Proceedings of the 59th Design Automation Conference (DAC 2021)},
}
@inproceedings{zhao_synthesizing_2021,
  author    = {Zelin Zhao and Yanyan Jiang and Chang Xu and Tianxiao Gu and Xiaoxing Ma},
  title     = {Synthesizing Object State Transformers for Dynamic Software Updates},
  pages     = {1111--1122},
  year      = {2021},
  booktitle = {Proceedings of the 43rd ACM/IEEE International Conference on Software Engineering (ICSE 2021)},
  award     = {ACM SIGSOFT Distinguished Paper Award and ACM Europe Council Best Paper Award}
}
@inproceedings{xu_commit_2019,
  title     = {Commit Message Generation for Source Code Changes},
  author    = {Xu, Shengbin and Yao, Yuan and Xu, Feng and Gu, Tianxiao and Tong, Hanghang and Lu, Jian},
  booktitle = {Proceedings of the Twenty-Eighth International Joint Conference on Artificial Intelligence, {IJCAI-19}},
  pages     = {3975--3981},
  year      = {2019},
}
@inproceedings{gu_practical_2019,
  author    = {Tianxiao Gu and Chengnian Sun and Xiaoxing Ma and Chun Cao and Chang Xu and Yuan Yao and Qirun Zhang and Jian Lu and Zhendong Su},
  title     = {Practical GUI Testing of Android Applications via Model Abstraction and Refinement},
  pages     = {269 -- 280},
  year      = {2019},
  booktitle = {Proceedings of the 41st ACM/IEEE International Conference on Software Engineering (ICSE 2019)},
  pdf       = {/static/ape-icse-2019.pdf},
  code      = {/ape},
}
~~~

[More...](./publications)

----------------
## Research Interests and Projects

* Programming Languages
    * [fastFFI](https://github.com/alibaba/fastffi): Modern and Efficient FFI for Java and C++.
        * [llvm4jni](https://github.com/alibaba/fastFFI/tree/main/llvm4jni): A tool that can translate LLVM bitcode into Java bytecode.
    * AOT & JWarmup: Towards a Serverless Java Runtime
* Java Virtual Machine
    * [Bytecode generator](./testing/jvm/)
        * [Reported bugs](./testing/jvm/)
    * <a href="https://bitbucket.org/txgu/ape"><i class="fab fa-bitbucket"></i></a> [Ape](./ape/): Automated Testing of Android Applications with Abstraction Refinement.
    * <a href="https://bitbucket.org/txgu/javelus"><i class="fab fa-bitbucket"></i></a> [MiniTracing](./minitracing/)
        * A whole program tracing tool that can trace method entrance/exit, object allocation, GC moving, and locking/unlocking events in the JVM.
        * Checkout the branch `mini-tracing` of `javelus`
        * Other tools based on this project:
            * [PHD](https://bitbucket.org/txgu/phd): Precise Heap Differentiating: An experimental tool aiming at precisely differentiating two heap snapshots.
* Android Application Testing
    * [Ape](./ape): A framework for model-based testing for Android apps.
    * WGDroid: A fancy GUI exploration tool developed on top of Ape.
    * [AimDroid](https://icsnju.github.io/AimDroid-ICSME-2017/)
    * MiniTracing: Collect method/coverage without bytecode instrumentation.
        * [Android 6 (binary for x86)](art-mt-x86.zip): Android ART with method/instruction coverage support.
        * [Android 4.4 (binary for x86)](dalvikvm-mt-x86.zip): Android Dalvik VM with method/instruction coverage support.
        * [android-mt-cmd](https://bitbucket.org/txgu/android-mt-cmd): Command line tools to collect coverage.
        * [android-mt-parser](https://bitbucket.org/txgu/android-mt-parser): Parser for the coverage data.
* Dynamic Software Updating
    * <a href="https://bitbucket.org/txgu/javelus"><i class="fab fa-bitbucket"></i></a> [Javelus](./javelus/): Low-disruptive Dynamic Updating of Java Applications.
        * A dynamic-updating-enabled JVM built on top the HotSpot JVM in OpenJDK 8
    * A [list](./javelus/literature) of practical DSU tools.
    * <a href="https://bitbucket.org/txgu/aotes-asm"><i class="fab fa-bitbucket"></i></a> AOTES: Automating Object Transformations for Dynamic Software Updating via Execution Synthesis 
* [Compiler Testing](./testing/compiler/)
    * `pytkfuzz`: A python implementation of [`tkfuzz`](https://chengniansun.bitbucket.io/papers/issta16.pdf).

--------------------

# Activities

* Program Committee: ASE 2020, 2021; ASE Industry Showcase 2020, 2021; VIML 2021; Graal Workshop@CGO 2020, 2021; IEEE ATC 2018
* Artifact Evaluation Committee: ECOOP 2019; ISSTA 2019
* Reviewer: TOSEM, TSE, TPDS, JCST, FCS, CSUR, ICECCS, IEEE ATC, TACAS

