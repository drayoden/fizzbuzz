#!/usr/bin/env python

print("--fizzbuzz--")

for i in range(1,101):
    str = i
    three = False
    if ( i % 3 == 0 ):
        str = "fizz"
        three = True
    if ( i % 5 == 0):
        if three:
            str += "buzz"
        else:
            str = "buzz"

    print("{}".format(str))
