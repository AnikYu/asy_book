import threading 
import time

def print_fib(number):
    def fib(n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    fib(number)

def fibs_with_threads():
    fortieth_thread = threading.Thread(target=print_fib, args=(40, ))
    f0rty_first_thread = threading.Thread(target=print_fib, args=(41, ))    
    
    fortieth_thread.start()
    f0rty_first_thread.start()
    
    fortieth_thread.join()
    f0rty_first_thread.join()

start_threads = time.time()
fibs_with_threads()
end_threads = time.time()
print(f'Многопоточное вычисление заняло {end_threads - start_threads:.4f} с.')