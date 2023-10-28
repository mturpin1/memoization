import time
from ..utils import print_execution_time

fib_cache = {}

def fibonacci(n, cache):
    if n in cache:
        return cache[n]
    if n < 2:
        return n
    result = fibonacci(n-1, cache) + fibonacci(n-2, cache)
    cache[n] = result
    return result

@print_execution_time
def main():
    fib_sequence = int(input('Please input the numerical position in the Fibonacci sequence you would like to calculate to and/or return:   '))

    print(fibonacci(fib_sequence, fib_cache))

if __name__ == '__main__':
    main()

    while True:
        restart = input('Would you like to try again with a different number? (y/n)').lower()
    
        if restart == 'y':
            main()
        else:
            break
    

