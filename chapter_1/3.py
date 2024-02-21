import threading

def hello_from_thread():
    print(f'hi from thread {threading.current_thread().name}')
    
hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()

total_threads = threading.active_count() # 2
thread_name = threading.current_thread().name

print(f'В данный момент {total_threads}')
print(f'Name current {thread_name}')
hello_thread.join() # останавливаем поток
print(threading.active_count()) # 1