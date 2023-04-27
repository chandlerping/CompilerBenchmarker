from src.nbp_benchmarker import *
from src.tsvc_benchmarker import *


def main():
    # nbp_b = NBPBenchmarker()
    # nbp_b.set_test('ft', 'S', 'li')

    tsvc_b = TSVCBenchmarker()
    tsvc_b.set_test('novec', 'default', 'lu')

if __name__ == '__main__':
    main()
