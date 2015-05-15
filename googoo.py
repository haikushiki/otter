#!python3

import sys
from random import randint

x = int(sys.argv[1]) if sys.argv[1].isdigit() else randint(1, 10)

while (x > 0):
    print("goo")
    x-=1;
