import os


def extract_flags(flags):
    s = ''
    for f in flags:
        s += ' '
        s += f
    return s


def check_size(dir):
    return os.path.getsize(dir)
