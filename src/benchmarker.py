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
        self.generate_config('clang')
        self.benchmark()
        result_gcc = self.report()
        self.generate_config('gcc')
        self.benchmark()
        result_llvm = self.report()
        print(result_gcc, result_llvm)
