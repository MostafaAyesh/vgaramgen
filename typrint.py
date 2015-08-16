# Cool Way To Print In Python 'typrint'
import sys, time
def typrint(word):
    for i in word:
        sys.stdout.write(i)
        time.sleep(0.04)
    sys.stdout.write('\n')
