import os
import threading

print('python process id', os.getpid())

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'In current count {total_threads}')
print(f'Name current {thread_name}')
