from bs4 import BeautifulSoup
import requests

url = 'https://albuquerque.craigslist.org/search/sof'
response = requests.get(url)
print(response)

data = response.text
soup = BeautifulSoup(data, 'html.parser')

jobs = soup.find_all('p', {'class':'result-info'})

for job in jobs:
    title = job.find_all('a', {'class':'result-title'})
    address = job.find_all('span', {'class':'result-hood'})
    print(title + ': ' + address)