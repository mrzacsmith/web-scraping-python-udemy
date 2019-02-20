from bs4 import BeautifulSoup
import requests

url = 'https://albuquerque.craigslist.org/search/sof'
response = requests.get(url)
print(response)

data = response.text
soup = BeautifulSoup(data, 'html.parser')

jobs = soup.find_all('p', {'class':'result-info'})

for job in jobs:
    title = job.find('a', {'class':'result-title'}).text
    location_tag = job.find('span', {'class':'result-hood'})
    location = location_tag.text[1:-1] if location_tag else 'N/A'
    date = job.find('time', {'class':'result-date'}).text
    link = job.find('a', {'class':'result-title'}).get('href')

    job_response = requests.get(link)
    job_data = job_response.text
    job_soup = BeautifulSoup(job_data, 'html.parser')
    job_description = job_soup.find('section', {'id':'postingbody'}).text
    job_attributes_tag = job_soup.find('p', {'class':'attrgroup'})
    job_attributes = job_attributes_tag.text[1:-1] if job_attributes_tag else 'N/A'

    print('Job: ' + title + ' : ' + location + ' : ' + date + "\n" + link + '\n' + job_description + '\n' + job_attributes + '\n------')