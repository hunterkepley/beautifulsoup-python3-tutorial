# This is an updated guide for Python 3.x from
# https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
# Python 3 had urllib2 moved into several different modules
from urllib.request import urlopen 
from bs4 import BeautifulSoup as bs
# for exporting as a csv
import csv
from datetime import datetime

# the url to scrape from, Linus Torvalds
linus_page = 'https://en.wikipedia.org/wiki/Linus_Torvalds'

# get the HTML page of the url declared
# query the website and return the html to the variable 'page'
page = urlopen(linus_page)

# parse the html using beautiful soup and store in variable 'soup'
soup = bs(page, 'html.parser')

# Take out the <div> of name and get it's value
name_box = soup.find('h1', attrs={'class': 'firstHeading'})

# After we have the tag ^ we can get the data by getting it's |text|
name = name_box.text.strip() # strip() is used to remove starting and trailing

# get the birthday of our boy Linus
birthday_box = soup.find('span', attrs={'class':'bday'})
birthday = birthday_box.text.strip()
#print(name) # Unprint to see live
#print(birthday) # Unprint to see live

# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name, birthday, datetime.now()])