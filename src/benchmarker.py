class Benchmarker:
    # li lu dl sm
    group = ''
    compilers = ['gcc', 'clang']
    output = []

    def generate_config(self, compiler):
        pass

    def benchmark(self):
        pass

    def report(self):
        # return [filesize, time]
        return []
        pass

    def run(self):
        self.generate_config('gcc')
        self.benchmark()
        result_gcc = self.report()
        self.generate_config('llvm')
        self.benchmark()
        result_llvm = self.report()

        print('\n\n\n Comparing opt group ', self.group)
        print('gcc')
        print('file size ', result_gcc[0], '    executiion time', result_gcc[1])
        print('llvm')
        print('file size ', result_llvm[0], '    executiion time', result_llvm[1])
