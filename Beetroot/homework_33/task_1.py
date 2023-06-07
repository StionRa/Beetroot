import requests

url = 'https://www.wikipedia.org/robots.txt'
filename = 'robots.txt'

response = requests.get(url)
if response.status_code == 200:
    with open(filename, 'w') as file:
        file.write(response.text)
    print(f'Successfully downloaded and saved {filename}')
else:
    print(f'Failed to download {filename}. Status code: {response.status_code}')
