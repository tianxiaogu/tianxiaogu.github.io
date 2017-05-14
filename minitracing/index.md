title: Whole Program Tracing in JVM


# Whole Program Tracing in JVM


## Source

1. MiniTracing (the `mini-tracing` branch in the [Javelus](https://bitbucket.org/javelus/javelus/))
2. [PHD](https://bitbucket.org/txgu/phd)
    * If you only want to trace locking/unlocking events, only the [concurrent-lock-hooks](https://bitbucket.org/txgu/phd/src/master/concurrent-lock-hooks/) is sufficient.

## Build

Checkout the [build instructions](../javelus/) of Javelus.

## Install

1. Windows
    * Replace the built `jvm.dll` in your local JDK or JRE installation.
2. Linux
    * Check the script `hotspot` in your built directory.

## Run

### Method Trace

To be added.

### Lock Trace

We mainly trace locking and unlocking of the following locks.

1. Monitors by the `synchronized` keyword.
2. Locks in the package `java.util.concurrent.locks`.

The following options should be assigned when starting the JVM (MiniTracing).

1. Enable MiniTracing

    ```
    -XX:+EnableMiniTracing
    -XX:+MiniTracingGlobalLogger
    -XX:+MiniTracingLockAcquire
    -XX:+MiniTracingLockRelease
    -XX:+MiniTracingObjectAlloc
    -XX:+MiniTracingForwardPointers
    ```

2. Disable JVM optimizations

    ```
    -XX:-TieredCompilation
    -XX:+UseHeavyMonitors
    -XX:EmitSync=5
    -XX:-UseCompressedOops
    -XX:-UseCompressedClassPointers
    -XX:-DoEscapeAnalysis
    ```

3. Replace the implementation of locks in the package `java.util.concurrent.locks`.

    For the modified implementation,
    check <https://bitbucket.org/txgu/phd/src/master/concurrent-lock-hooks/>.

    ```
    -Xbootclasspath/p:<path-to->
    ```

Feel free to contact me if you have any problem in running this easy-to-use tracer for locks in the HotSpot JVM.
