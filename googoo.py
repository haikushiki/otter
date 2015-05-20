#!python3

import sys
from random import randint
i = input("Give us a number from 1 to 10 dear: ")
x = int(i) if i.isdigit() else randint(1, 10)

while (x > 0):
    print("goo")
    x-=1;
