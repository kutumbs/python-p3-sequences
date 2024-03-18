#!/usr/bin/env python3

def print_fibonacci(length):
     if length == 0:
        print([])
        return []
     elif length == 1:
        print([0])
        return [0]
     elif length == 2:
        print([0, 1])
        return ([0, 1])

     fib_list = [0, 1]
     while len(fib_list) < length:
        fib_list.append(fib_list[-1] + fib_list[-2])
     print(fib_list)
     return fib_list