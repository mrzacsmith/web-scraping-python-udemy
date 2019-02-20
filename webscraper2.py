from bs4 import BeautifulSoup
import requests

url =  'https://albuquerque.craigslist.org/search/sof'
response = requests.get(url)
print(response)

data = response.text
# print(data)

soup = BeautifulSoup(data, 'html.parser')
# print(soup)

titles = soup.find_all('a', {'class':'result-title'})
for title in titles:
    print(title.text)

addresses = soup.find_all('span', {'class':'result-hood'})

for address in addresses:
    print(address.text)