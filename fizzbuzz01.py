#!/usr/bin/env python

print("--fizzbuzz--")

for i in range(1,101):
    str = i
    three = False
    if ( i % 3 == 0 ):
        str = "Fizz"
        three = True
    if ( i % 5 == 0):
        if three:
            str += "Buzz"
        else:
            str = "Buzz"

    print("{}".format(str))
