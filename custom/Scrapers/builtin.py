from bs4 import BeautifulSoup
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from threading import Thread
import requests, threading, sys

chi = 'https://www.builtinchicago.org/jobs/?f[0]=job-category_data-analytics&hash-changes=3&page=0'
nyc = 'https://www.builtinnyc.com/jobs/?f[0]=job-category_data-analytics&hash-changes=3&page=0'
sea = 'https://www.builtinseattle.com/jobs/?f[0]=job-category_data-analytics&hash-changes=3&page=0'
sf = 'https://www.builtinsf.com/jobs/?f[0]=job-category_data-analytics&hash-changes=3&page=0'
jobPages = []

def pull(url):
	r = requests.get(url)
	if r.status_code == 200:

		soup = BeautifulSoup(r.text, 'html.parser')
		for a in soup.find_all('a', href=True): 
			if '/job/data' in a['href']:
				jobPages.append({'url':url.split('jobs')[0],'uri':a['href']})
	else:
		print('Can\'t pull data ', url)

def getJobDesc():
	

def ripInfo(url):
	r = requests.get(url['url']+url['uri'])
	if r.status_code == 200:
		soup = BeautifulSoup(r.text, 'html.parser')
		jobTitle = soup.find_all(text=True,class_="field field--name-title field--type-string field--label-hidden")
		jobDescription = soup.find_all(class_='job-description fade-out').get_text()
		print(jobDescription)
		sys.exit()
		#jobDescription= soup2.find_all(class_='job-description fade-out')
		jobDescription = str(jobDescription).replace('<strong>','').replace('<p>','').replace('</p>','')
		jobDescription = jobDescription.replace('<ul>','').replace('<b>','').replace('</b>','').replace('</ul>','')
		print(jobDescription)
	else:
		print('Can\'t pull data ', url)

t1 = threading.Thread(target=pull, args=(chi,)) 
t2 = threading.Thread(target=pull, args=(nyc,)) 
t3 = threading.Thread(target=pull, args=(sea,))
t4 = threading.Thread(target=pull, args=(sf,))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join() 
t2.join() 
t3.join() 
t4.join() 

print(jobPages[0])
ripInfo(jobPages[0])
sys.exit()
with ThreadPoolExecutor() as executor:

	executor.map(ripInfo, jobPages, timeout=30)

