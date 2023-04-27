from src.benchmarker.benchmarker import Benchmarker
from src.utils import *
from src.opt_group import *
import subprocess


class BEEBSBenchmarker(Benchmarker):
    def __init__(self):
        FNULL = open(os.devnull, 'w')
        os.chdir('beebs')
        subprocess.run('./configure', shell=True,stdout=FNULL,stderr=FNULL)
        subprocess.run('make', shell=True,stdout=FNULL,stderr=FNULL)
        os.chdir("../")

    def set_test(self, test, group):
        print("Benchmark: beebs")
        self.test = test
        self.group = group
        self.run()

    def generate_config(self, compiler):
        f = open("beebs/src/" + str(self.test) + "/Makefile", "r")
        lines = f.readlines()
        f.close()
        cid = 0
        if compiler == 'llvm':
            cid = 1

        if self.group == 'li':
            flags = extract_flags(li[cid])
        elif self.group == 'lu':
            flags = extract_flags(lu[cid])
        elif self.group == 'dl':
            flags = extract_flags(dl[cid])
        else:
            flags = extract_flags(sm[cid])

        for i in range(0,len(lines)):
            if "AM" not in lines[i] and "CC = " in lines[i]:
                lines[i] = "CC = {}\n".format(self.compilers[cid])
            elif "CCAS = " in lines[i]:
                lines[i] = "CCAS = {}\n".format(self.compilers[cid])
            elif "CCASDEPMODE = " in lines[i]:
                lines[i] = "CCASDEPMODE = -depmode={}\n".format(self.compilers[cid])
            elif "CCDEPMODE = " in lines[i]:
                lines[i] = "CCDEPMODE = -depmode={}\n".format(self.compilers[cid])
            elif "CPP = " in lines[i]:
                lines[i] = "CPP = {} -E\n".format(self.compilers[cid])
            elif "ac_ct_CC = " in lines[i]:
                lines[i] = "ac_ct_CC = {}\n".format(self.compilers[cid])                
            elif "AM" not in lines[i] and "CPPFLAGS = " in lines[i]:
                lines[i] = "CPPFLAGS = -Wno-unused-command-line-argument " + flags + "\n"
        
        f = open("beebs/src/" + str(self.test) + "/Makefile", "w+")
        f.writelines(lines)
        f.close()

    def benchmark(self, compiler):
        print("\nPERFORMING COMPILATION FOR BEEBS TEST: " + str(compiler) + " " + str(self.test) + " " + str(self.group))
        FNULL = open(os.devnull, 'w')
        os.chdir('beebs/src/' + str(self.test))
        subprocess.run('make clean', shell=True,stdout=FNULL,stderr=FNULL)
        subprocess.run('make', shell=True, stdout=FNULL,stderr=FNULL)
        self.iterations = 50
        print("RUNNING PROGRAM AND TIMING FOR " + str(compiler) + " " + str(self.test) + " " + str(self.group))
        cmd = "for i in {1.." + str(self.iterations) + "}; do time ./" + str(self.test) + "; done 2>&1 | grep ^real | sed -e s/.*m// | awk '{sum += $1} END {print sum / NR}'"
        process = subprocess.Popen(cmd, shell=True, executable="/bin/bash", text=True,stdout=subprocess.PIPE)
        self.output, err = process.communicate()   
        os.chdir('../../..')

    def report(self):
        os.chdir('src/' + str(self.test))
        file_size = check_size(str(self.test))
        os.chdir('../../../..')
        return file_size, self.output
