from bs4 import BeautifulSoup
import requests

url = 'https://www.programmableweb.com/apis/directory'
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')



apis = soup.find_all('div', {'class':'tbody'})

for api in apis:
    print(api)
