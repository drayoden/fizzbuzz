#!/usr/bin/env python3

print ("~~~ fizzbuzz ~~~")
for i in range(1,101):
    res = ''
    if i % 3 == 0:
        res += "Fizz"
    if i % 5 == 0:
        res += "Buzz"
    print(res or i)
