# loop invariants 0 for gcc 1 for llvm
li = [[], []]
li[0]= [
    '-fira-loop-pressure',
    '-ftree-loop-im',
    '-fmove-loop-invariants',
    # '-fmove-loop-stores'
]
li[1] = ['-licm']

# loop unroll
lu = [[], []]
lu[0] = [
    '-ftree-loop-ivcanon',
    '-faggressive-loop-optimizations',
    '-floop-unroll-and-jam',
    '-funroll-loop',
    '-funroll-all-loops'
]
lu[1] = [
    '-loop-unroll',
    '-loop-unroll-and-jam'
]

# dead loops
dl = [[], []]
dl[0] = [
    '-ffinite-loops',
    '-fsplit-paths'
]
dl[1] = ['-loop-deletion']

# structure & memory
sm = [[], []]
sm[0] = [
    '-floop-nest-optimize',
    '-ftree-loop-optimize',
    '-ftree-loop-distribution'
]
sm[1] = [
    '-loop-reduce',
    '-loop-simplify'
]