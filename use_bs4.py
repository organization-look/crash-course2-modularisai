import requests
from bs4 import BeautifulSoup

url = 'https://www.detik.com'

try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'sukses{response.status_code}')
        # print(f'Content{response.text}')
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f'judul: {url}')

        print(f'Title: {soup.title.string}')

    else:
        print(f'ada kesalahan{response.status_code}')
except Exception as e:
    print(f'error{e}')

print('program end')
