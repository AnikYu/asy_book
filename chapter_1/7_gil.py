import time
import requests

def read_example():
    response = requests.get('https://www.example.com')
    print(response.status_code)
    
syncc_start = time.time()

read_example()
read_example()

sync_end = time.time()

print(f'Synchronic time {sync_end - syncc_start:.4f}')