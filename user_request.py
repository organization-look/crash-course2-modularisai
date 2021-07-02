import requests

url = 'https://www.detik.com'

try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'sukses{response.status_code}')
        print(f'Content{response.text}')
    else:
        print(f'ada kesalahan{response.status_code}')
except Exception as e:
    print(f'error{e}')

print('program end')
