#!/usr/bin/env python3

def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


f100 = fib(1000000000000)
print(len(f100))
