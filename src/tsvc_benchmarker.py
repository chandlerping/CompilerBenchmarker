from src.benchmarker import Benchmarker
from src.utils import *
from src.opt_group import *
import subprocess


class TSVCBenchmarker(Benchmarker):
    group = ''
    mode = ''  # vec, novec
    test = ''  # relaxed, precised, default
    file_size = 0

    def set_test(self, mode, test, group):
        self.test = test
        self.group = group
        self.mode = mode
        self.run()

    def generate_config(self, compiler):
        if compiler == 'gcc':
            cid = 0
            f_dir = "./TSVC_2/makefiles/Makefile.GNU"
            li_no = 4
        else:
            cid = 1
            f_dir = "./TSVC_2/makefiles/Makefile.clang"
            li_no = 5

        f = open(f_dir, "r")
        lines = f.readlines()
        f.close()

        if self.group == 'li':
            flags = extract_flags(li[cid])
        elif self.group == 'lu':
            flags = extract_flags(lu[cid])
        elif self.group == 'dl':
            flags = extract_flags(dl[cid])
        else:
            flags = extract_flags(sm[cid])

        lines[li_no] = 'CFLAGS	= -Wno-unused-command-line-argument ' + flags + '\n'
        f = open(f_dir, "w+")
        f.writelines(lines)
        f.close()

    def benchmark(self, compiler):
        print("PERFORMING COMPILATION FOR TSVC_2 TEST: " + str(compiler) + " " + self.mode + " " + str(self.test) + " " + str(self.group))
        FNULL = open(os.devnull, 'w')
        os.chdir('TSVC_2')

        if compiler == 'gcc':
            subprocess.run("make COMPILER={}".format('GNU'), shell=True, stdout=FNULL, stderr=FNULL)
            os.chdir('bin/GNU')
        else:
            subprocess.run("make COMPILER={}".format('clang'), shell=True, stdout=FNULL, stderr=FNULL)
            os.chdir('bin/clang')

        self.file_size = check_size('tsvc_{}_{}'.format(self.mode, self.test))
        cmd = './' + 'tsvc_{}_{}'.format(self.mode, self.test)
        print("")
        self.output = subprocess.getoutput(cmd).split('\n')
        os.chdir('../../..')

    def report(self):
        os.chdir('TSVC')
        ex_time = 0
        for line in self.output:
            if "Loop" not in line:
                ex_time += float(line.split()[1])
        os.chdir('..')
        return self.file_size, ex_time
