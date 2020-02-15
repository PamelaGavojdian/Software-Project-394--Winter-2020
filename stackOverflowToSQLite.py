import urllib.parse
import requests
import xmltodict
import sqlite3

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


def SQLiteFromDict(inputDict, city):

    conn = sqlite3.connect('StackOverflowJobs.db')
    c = conn.cursor()

    formattedCity = city.split(',')[0].replace(' ', '_')

    tableName = "jobs_in_" + formattedCity
    c.execute('''CREATE TABLE IF NOT EXISTS {} (title text, link text)'''.format(tableName))

    for listing in inputDict:

        execStr = '''INSERT INTO {} VALUES ("{}", "{}")'''.format(tableName, listing['title'], listing['link'])

        c.execute(execStr)

    conn.commit()
    conn.close()

    return


def createTableforCity(city, radius):
    url = createUrl(city, radius)
    jobDict = getDictFromURL(url)
    SQLiteFromDict(jobDict, city)


for city in ["Chicago, IL, USA", "Los Angeles, IL, USA", "New York, NY, USA"]:
    createTableforCity(city, 20)