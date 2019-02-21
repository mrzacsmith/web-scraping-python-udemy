# Based on what you have leaned in this course, web scrape the API lists on this page, and export your result into a CSV file.

# https://www.programmableweb.com/apis/directory

# Your Python code should scrape the following details from each table row:

# • API Name
# • API (absolute) URL
# • API Category
# • API Description

# Your Python code should crawl to all the available "next" pages. Your final result should be approx. 20,699 rows.

# On your machine, write the code and test it to make sure it is working. Then copy paste your final code here.

# All the best!

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.programmableweb.com/apis/directory'
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')

npo_apis = {}
api_no = 0

response = requests.get(url)
data = response.text
soup = BeautifulSoup(data,'html.parser')


while True:
    apis = soup.find('table', {'class': 'views-table cols-4 table'}).find('tbody').find_all('tr')
    for api in apis:
        name = api.find('td', {'class': 'views-field views-field-title col-md-3'}).find('a').text
        urls = api.find('td', {'class': 'views-field views-field-title col-md-3'}).find('a').get('href')
        category = api.find('td', {'class': 'views-field views-field-field-article-primary-category'}).find('a').text
        description = soup.find('td', {
            'class': 'views-field views-field-search-api-excerpt views-field-field-api-description hidden-xs visible-md visible-sm col-md-8'}).text
        api_no += 1
        print(api_no)
        npo_apis[api_no]= [name, urls, category, description]

        url_tag = soup.find('a', {'title': 'Go to next page'})
    if url_tag.get('href'):
        url = 'https://www.programmableweb.com/' + url_tag.get('href')
        print(url)
    else:
        break


print("Total API:", api_no)
df = pd.DataFrame.from_dict(npo_apis, orient = 'index', columns = ['API Name','API (absolute) URL','API Category', 'API Description'])


df.head()


df.to_csv('api.csv')