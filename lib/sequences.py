#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = []
    if length > 0:
       fibonacci_sequence.append(0)
       if length > 1:
           fibonacci_sequence.append(1)
           if length > 2:
               i = 2
               while i < length:
                   fibonacci_sequence.append(
                       fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
                   i += 1
    print(fibonacci_sequence)                    
    pass