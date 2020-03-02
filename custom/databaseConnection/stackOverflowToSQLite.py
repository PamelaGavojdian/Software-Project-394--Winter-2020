import urllib.parse
import requests
import xmltodict
import sqlite3
from bs4 import BeautifulSoup
from tqdm import tqdm 

def createUrl(city, range, salary=None, unit='Miles'):
    baseURL= """https://stackoverflow.com/jobs/feed"""
    queryList = []
    queryList.append(('l', city))
    queryList.append(('d', range))
    if salary:
        queryList.append(('s', salary))
    queryList.append(('u', unit))
    queryString = urllib.parse.urlencode(queryList)
    return baseURL + "?" + queryString


def getDictFromURL(url):
    pageContent = requests.get(url).content
    data = xmltodict.parse(pageContent)
    startOfListings = data['rss']['channel']['item']
    return startOfListings
        
    # The dict contains the following keys:
    #   guid
    #   link
    #   a10:author
    #   category
    #   title
    #   description
    #   pubDate
    #   a10:updated
    #   location


def SQLiteFromDict(inputDict, city, distance):

    conn = sqlite3.connect('StackOverflowJobs.db')
    c = conn.cursor()

    formattedCity = city.split(',')[0].replace(' ', '_')

    tableName = "jobs_in_" + formattedCity
    c.execute('''CREATE TABLE IF NOT EXISTS {} (title text, link text UNIQUE, description text, distance integer)'''.format(tableName))

    for listing in inputDict:

        cleanDescription = BeautifulSoup(listing['description'], "lxml").text.replace('"','“') # SQLite doesn't like quotations in the statement, so replace them with fancy quotations
        # print(cleanDescription)
        execStr = '''INSERT OR IGNORE INTO {} VALUES ("{}", "{}", "{}", "{}")'''.format(tableName, listing['title'], listing['link'], cleanDescription, distance)

        c.execute(execStr)

    conn.commit()
    conn.close()

    return


def createTableforCity(city, radius):
    url = createUrl(city, radius)
    jobDict = getDictFromURL(url)
    SQLiteFromDict(jobDict, city, radius)

def getAllJobs():
    for city in ["Chicago, IL, USA", "Los Angeles, CA, USA", "New York, NY, USA"]:
        print("city:", city)
        for dist in tqdm(range(1, 50 + 1)):
            createTableforCity(city, dist)

if __name__ == '__main__':
    getAllJobs()