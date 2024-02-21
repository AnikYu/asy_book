import  requests

response = requests.get('https://www.example.com') # ограничен производительностью ввода-вывода

items = response.headers.items()

headers = [f'{key}: {header}' for key, header in items] # ограничено быстродействием процессора

formatted_headers = '\n'.join(headers) # ограничено быстродействием процессора

with open('headers.txt', 'w') as file:
    file.write(formatted_headers) # ограничен производительностью ввода-вывода