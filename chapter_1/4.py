import multiprocessing
import os

def hello_from_proctss():
    print(f'Привет от дочернего процесса {os.getpid()}')
    
if __name__ == '__main__':
    hello_process = multiprocessing.Process(target=hello_from_proctss)
    hello_process.start()
    
    print(f'Привет от родительского {os.getpid()}')

    hello_process.join()