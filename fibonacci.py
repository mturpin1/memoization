import time

fib_cache = {}

def fibonacci(n, cache):
    if n in cache:
        return cache[n]
    if n < 2:
        return n
    result = fibonacci(n-1, cache) + fibonacci(n-2, cache)
    cache[n] = result
    return result


def main():
    fib_sequence = int(input('Please input the numerical position in the Fibonacci sequence you would like to calculate to and/or return:   '))

    srt = time.time() # start real time
    spt = time.process_time() # start process time

    print(fibonacci(fib_sequence, fib_cache))

    ert = time.time() # end real time
    ept = time.process_time() # end process time

    elapsed_real_time = (ert - srt) * 1000 # elapsed real time in ms
    elapsed_process_time = (ept - spt) * 1000 # elapsed process time in ms

    print(f'real time:    {elapsed_real_time}')
    print(f'process time: {elapsed_process_time}')

if __name__ == '__main__':
    main()

    while True:
        restart = input('Would you like to try again with a different number? (y/n)').lower()
    
        if restart == 'y':
            main()
        else:
            break
    

