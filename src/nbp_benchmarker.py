from src.benchmarker import Benchmarker
from src.utils import *
from src.opt_group import *
import subprocess
import re


class NBPBenchmarker(Benchmarker):
    test = 'ft'
    size = 'S'
    group = 'li'

    def set_test(self, test, size, group):
        self.test = test
        self.size = size
        self.group = group

    def generate_config(self, compiler):
        f = open("./NPB3.0-omp-C/config/make.def", "r")
        lines = f.readlines()
        f.close()
        cid = 0
        if compiler == 'clang':
            cid = 1
        lines[18] = "CC = {}\n".format(self.compilers[cid])
        lines[19] = "CLINK	= {}\n".format(self.compilers[cid])
        if self.group == 'li':
            flags = extract_flags(li[cid])
        elif self.group == 'lu':
            flags = extract_flags(lu[cid])
        elif self.group == 'dl':
            flags = extract_flags(dl[cid])
        else:
            flags = extract_flags(sm[cid])
        lines[24] = 'CFLAGS	= ' + flags + '\n'
        f = open("./NPB3.0-omp-C/config/make.def", "w+")
        f.writelines(lines)
        f.close()

    def benchmark(self):
        os.chdir('NPB3.0-omp-C')
        subprocess.run('mkdir bin', shell=True)
        subprocess.run('make ' + self.test + ' ' + self.size, shell=True)
        os.chdir('bin')
        cmd = './' + self.test + '.' + self.size
        self.output = subprocess.getoutput(cmd).split('\n')
        os.chdir('../..')

    def report(self):
        os.chdir('NPB3.0-omp-C')
        file_size = check_size('./bin/' + self.test + '.' + self.size)
        ex_time = 0
        for line in self.output:
            if "Time" in line:
                ex_time = line.split()[-1]
        os.chdir('..')
        return file_size, ex_time
