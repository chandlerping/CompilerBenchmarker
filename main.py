from src.nbp_benchmarker import *


def main():
    nbp_b = NBPBenchmarker()
    nbp_b.set_test('ft', 'S', 'li')
    nbp_b.run()


if __name__ == '__main__':
    main()
