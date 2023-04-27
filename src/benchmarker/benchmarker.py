class Benchmarker:
    # li lu dl sm
    group = ''
    compilers = ['gcc', 'clang']
    output = []

    def generate_config(self, compiler):
        pass

    def benchmark(self, compiler):
        pass

    def report(self):
        # return [filesize, time]
        return []
        pass

    def run(self):
        print("--------------------------------------------------------------------")
        self.generate_config('gcc')
        self.benchmark('gcc')
        result_gcc = self.report()
        self.generate_config('llvm')
        self.benchmark('llvm')
        result_llvm = self.report()

        print('\nComparing opt group: ', self.group)
        print('gcc: file size', result_gcc[0], '    execution time=', result_gcc[1], '\n')
        print('llvm: file size', result_llvm[0], '    execution time=', result_llvm[1], '\n')
        print("--------------------------------------------------------------------")
