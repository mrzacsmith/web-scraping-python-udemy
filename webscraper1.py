from bs4 import BeautifulSoup
import requests

url = 'https://albuquerque.craigslist.org/search/sof'
response = requests.get(url)
print(response)

data = response.text
# print(data)

soup = BeautifulSoup(data, 'html.parser')
print(soup)  

tags = soup.find_all('a')
for tag in tags:
    print(tag.get('href'))

