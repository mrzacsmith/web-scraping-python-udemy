from bs4 import BeautifulSoup
import requests
import pandas as pd


# Put URL, as example https://albuquerque.craigslist.org/ in main_url and the and the parameters in the specific url
main_url = 'https://albuquerque.craigslist.org/'
specific_url = 'search/sof'
url = main_url + specific_url

d = { 'key':'value'}
print(d)

d['new key'] = 'new value'
print(d)

npo_jobs = {}
job_count = 0
while True:  
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
        job_count += 1
        npo_jobs[job_count] = [title, location, date, link, job_description, job_attributes]
        print('Job: ' + title + ' : ' + location + ' : ' + date + "\n" + link + '\n' + job_description + '\n' + job_attributes + '\n------')
    
    url_tag = soup.find('a', {'title':'next page'})
    if url_tag.get('href'):
        url = main_url + url_tag.get('href')
        print(url)
    else:
        break

print('Job Count: ' + str(job_count))
npo_jobs_df = pd.DataFrame.from_dict(npo_jobs, orient = 'index', columns = ['Job Title', 'Location', 'Date', 'Link', 'Job Description', 'Job Attributes'])

print(npo_jobs_df.head())
npo_jobs_df.to_csv('npo_jobs.csv')