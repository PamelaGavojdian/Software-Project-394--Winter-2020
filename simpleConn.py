import sqlite3
from custom.objects.Job import Job
connection = sqlite3.connect('jobs.db')

c = connection.cursor()

"""
for row in c.execute('SELECT title FROM jobs_in_Chicago'):
    print(row)
"""
def inputPosition(position=""):
    if(position==""):
        return("")
    else:
        return position
def inputCity(location=""):
    if(location=="Los Angeles"):
        for row in c.execute('SELECT title FROM jobs_in_Los_Angeles'):
            print(row)
    elif(location=="Chicago"):
        for row in c.execute('SELECT title FROM jobs_in_Chicago'):
            print(row)
    elif(location==""):
        print("Location was empty.")
    else:
        print("Location not available.")

#ans = input("City? (Chicago, Los Angeles, New York, Boston, D.C.) ")
for row in c.execute('SELECT title, link FROM jobs_in_Chicago'):
    temp = Job("Boss", 0, "Chicago")
    print(temp.position)
