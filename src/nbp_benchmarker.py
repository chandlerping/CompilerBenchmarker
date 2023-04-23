from src.benchmarker import Benchmarker
from src.utils import *
from src.opt_group import *
import subprocess
import re


class NBPBenchmarker(Benchmarker):
    test = 'ft'
    size = 'S'

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

    def benchmark(self):
        os.chdir('NPB3.0-omp-C')
        subprocess.run('mkdir bin', shell=True)
        subprocess.run('make ' + self.test + ' ' + self.size, shell=True)
        os.chdir('bin')
        cmd = './' + self.test + '.' + self.size
        self.output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
        print(self.output)
        os.chdir('../..')

    def report(self):
        os.chdir('NPB3.0-omp-C')
        file_size = check_size('./bin/' + self.test + '.' + self.size)
        ex_time = 0
        for line in self.output:
            if 'Time in seconds' in line:
                ex_time = line.split()[-1]
                print(line)
        os.chdir('..')
        return file_size, ex_time
