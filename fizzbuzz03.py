#!/usr/bin/env python3

# NOTE: not very Pythonistic... not very readable or stylistic but it does work.

print ("~~~ fizzbuzz ~~~")
for i in range(1,101):
    print("fizzbuzz") if (i % 15 == 0) else print("buzz") if (i % 5 == 0) else print("fizz") if (i % 3 == 0) else print(i)
