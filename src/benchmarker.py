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
        pass

    def run(self):
        print('\n Comparing opt group ', self.group)
        self.generate_config('gcc')
        self.benchmark()
        print('gcc')
        result_gcc = self.report()
        print(result_gcc)
        self.generate_config('llvm')
        self.benchmark()
        print('llvm')
        result_llvm = self.report()
        print(result_llvm)
