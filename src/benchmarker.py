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
        self.generate_config('gcc')
        self.benchmark()
        result_gcc = self.report()
        self.generate_config('llvm')
        self.benchmark()
        result_llvm = self.report()

        print('\n\n\n Comparing opt group ', self.group)
        print('gcc')
        print(result_gcc)
        print('llvm')
        print(result_llvm)
