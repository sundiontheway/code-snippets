# coding: utf-8
from sys import stdout
import time

def progress(width, percent):
    """ ====       4/51 """

    if percent > 100:
        stdout.write('')
        stdout.flush()
        return

    print_str = "%s %d/%d\r" % \
        (('%%-%ds' % width) % (width * percent / 100 * '='), percent, width)

    stdout.write(print_str)
    stdout.flush()

def progress_100(percent):
    """ =====       5%  """

    if percent > 100:
        stdout.write('')
        stdout.flush()
        return

    print_str = "%s %d%%\r" % \
        (('%%-%ds' % 100) % (100 * percent / 100 * '='), percent)

    stdout.write(print_str)
    stdout.flush()


if __name__ == "__main__":
    for i in range(1, 100):
        # progress_100(i)
        progress(120, i)
        time.sleep(1)



