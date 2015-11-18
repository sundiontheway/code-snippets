# coding: utf-8
from sys import stdout
import time

def progress(width, percent):
    """ 终端进度条 """

    if percent > 100:
        stdout.write('')
        stdout.flush()
        return

    print_str = "%s %d%%\r" % \
        (('%%-%ds' % width) % (width * percent / 100 * '='), percent)

    stdout.write(print_str)
    stdout.flush()

if __name__ == "__main__":
    for i in range(1, 100):
        progress(100, i)
        time.sleep(1)



