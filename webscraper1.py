from bs4 import BeautifulSoup
import requests

url = 'https://albuquerque.craigslist.org/d/real-estate/search/rej'
response = requests.get(url)
print(response)

data = response.text
# print(data)

soup = BeautifulSoup(data, 'html.parser')
print(soup)
