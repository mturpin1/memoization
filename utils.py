import time

def time_execution(func):
    def wrapper(*args, **kwargs):
        srt = time.time()
        spt = time.process_time()

        result = func(*args, **kwargs)

        ert = time.time()
        ept = time.process_time()

        elapsed_real_time = (ert - srt) * 1000
        elapsed_process_time = (ept - spt) * 1000

        print(f'real time:    {elapsed_real_time}')
        print(f'process time: {elapsed_process_time}')

        return result
    return wrapper

@time_execution
def test_func(input="Test"):
    print(f'{input}')

test_func("test input")
