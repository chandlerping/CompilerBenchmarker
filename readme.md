# CompilerBencharker
This is a framework to compare loop optimizations in llvm (clang) and gcc.
## Optimizations
Optimizations are grouped by their usages. Here we focus on loop optimizations which can be categorized into loop invariants, dead loops, unrolling loops and structure & memory.
The grouping can be found in ```src/utils```.
## Benchmark
Benchmark programs include NPB3.0, TSVC2 (TBD), BEEBS (TBD).
## Running
```main.py``` is a small demo.