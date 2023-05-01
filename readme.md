# CompilerBenchmarker
This is a framework to compare loop optimizations in llvm (clang) and gcc. The broader use is intended to allow users to create optimization groupings and import benchmark sets to provide repeatable testing for granular optimization groupings. 
## Optimizations
Optimizations are grouped by their usages. Here we focus on loop optimizations which can be categorized into loop invariants, dead loops, unrolling loops and structure & memory.
The grouping can be found in ```src/opt_group.py```.
The loops groupings are an example implementation, and the intended purpose is to demonstrate what groupings would look like. In practice users can define their own groupings for their specific applications and test them to see results.
## Benchmark
Benchmark programs include NPB3.0, TSVC2, BEEBS. These are three benchmarks representing different program types to avoid biasing our initial testing with loop optimizations, NPB3.0 represents scientific computing, TSVC2 represents vector optimizations, BEEBS represents embedded computing.
In practice, these benchmarks would be chosen by the user to align with their specific application the are testing optimizations on.
## Running
```main.py``` is a small demo. It shows how each of the different benchmarks can be used. For this particular demo it is useful for the user to know the following:

In order to set up a benchmark it first must be initialized, for example:
```python
nbp_b = NBPBenchmarker()
```

Then to create a test, each benchmark class is based off of the template ```benchmarker.py``` class. Thus, all have the function ```set_test(name, size, opt_group)```. It can be used as follows:
```python
nbp_b.set_test('ft', 'A', 'li')
```
NOTE: Each benchmark has different grouping in terms of name and size, but all use the optimization groupings as described: li (loop invariants), lu (loop unrolling), dl (dead loops), sm (loop structure and memory), and base (O0). These groupings can be defined in ```src/opt_group.py```. The different names and sizes are described below for the demo benchmarks.

Running this test as described will compile with the given grouping and time the resulting test.

## Benchmark Details

### NPB3.0
names: bt cg ep ft is lu mg sp

sizes: S W A B C 

### TSVC2
names: novec

sizes: default

### BEEBS
names: aha-compress aha-mont64 bs bubblesort cnt compress cover crc crc32 ctl ctl-stack ctl-string ctl-vector cubic dijkstra dtoa duff edn expint fac fasta fdct fibcall fir frac huffbench insertsort janne_complex jfdctint lcdnum levenshtein ludcmp matmult matmult-float matmult-int mergesort miniz minver nbody ndes nettle-aes nettle-arcfour nettle-cast128 nettle-des nettle-md5 nettle-sha256 newlib-exp newlib-log newlib-mod newlib-sqrt ns nsichneu picojpeg prime qrduino qsort qurt recursion rijndael select sglib-arraybinsearch sglib-arrayheapsort sglib-arrayquicksort sglib-arraysort sglib-dllist sglib-hashtable sglib-listinsertsort sglib-listsort sglib-queue sglib-rbtree slre sqrt st statemate stb_perlin stringsearch1 strstr tarai template trio trio-snprintf trio-sscanf ud whetstone wikisort         

sizes: default

## More Information
The paper that describes this framework is attached in ```docs/paper.pdf```