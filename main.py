from src.benchmarker.nbp_benchmarker import *
from src.benchmarker.tsvc_benchmarker import *
from src.benchmarker.beebs_benchmarker import *

#####################################################################################
#                               NBP BENCHMARK OPTIONS                               #
#   where <benchmark-name> is "bt", "cg", "ep", "ft", "is", "lu", "mg", or "sp"     #
#                                                                                   #
#   where <size> is "S", "W", "A", "B" or "C"                                       #
#####################################################################################

#####################################################################################
#                               BEEBS BENCHMARK OPTIONS                             #
# where <benchmark-name> is:                                                        #
# aha-compress aha-mont64 bs bubblesort cnt compress cover crc crc32 ctl            #
# ctl-stack ctl-string ctl-vector cubic dijkstra dtoa duff edn expint fac           #
# fasta fdct fibcall fir frac huffbench insertsort janne_complex jfdctint           #
# lcdnum levenshtein ludcmp matmult matmult-float matmult-int mergesort             #
# miniz minver nbody ndes nettle-aes nettle-arcfour nettle-cast128                  #
# nettle-des nettle-md5 nettle-sha256 newlib-exp newlib-log newlib-mod              #
# newlib-sqrt ns nsichneu picojpeg prime qrduino qsort qurt recursion               #     
# rijndael select sglib-arraybinsearch sglib-arrayheapsort sglib-arrayquicksort     #
# sglib-arraysort sglib-dllist sglib-hashtable sglib-listinsertsort sglib-listsort  #
# sglib-queue sglib-rbtree slre sqrt st statemate stb_perlin stringsearch1 strstr   #
# tarai template trio trio-snprintf trio-sscanf ud whetstone wikisort               #
#####################################################################################

def main():
    nbp_b = NBPBenchmarker()
    nbp_b.set_test('ft', 'A', 'li')

    # # only use the first 4 tests in TSVC_2 for time concern, can uncomment more tests in "./TSVC_2/src/tsvc.c"
    tsvc_b = TSVCBenchmarker()
    tsvc_b.set_test('novec', 'default', 'lu')

    beebs = BEEBSBenchmarker()
    beebs.set_test('dijkstra', 'default', 'dl')

if __name__ == '__main__':
    main()
