# This is an updated guide for Python 3.x from
# https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
# Python 3 had urllib2 moved into several different modules
from urllib.request import urlopen 
from bs4 import BeautifulSoup as bs
# for exporting as a csv
import csv
from datetime import datetime

# the url to scrape from, Linus Torvald, and now, his father *evil laugh*
urls = ['https://en.wikipedia.org/wiki/Linus_Torvalds',
    'https://en.wikipedia.org/wiki/Nils_Torvalds']

data = []
# make it into a for loop

for pg in urls:
    # get the HTML page of the url declared
    # query the website and return the html to the variable 'page'
    page = urlopen(pg)

    # parse the html using beautiful soup and store in variable 'soup'
    soup = bs(page, 'html.parser')

    # Take out the <div> of name and get it's value
    name_box = soup.find('h1', attrs={'class': 'firstHeading'})

    # After we have the tag ^ we can get the data by getting it's |text|
    name = name_box.text.strip() # strip() is used to remove starting and trailing

    # get the birthday of our boy Linus and his dad
    birthday_box = soup.find('span', attrs={'class':'bday'})
    birthday = birthday_box.text.strip()
    print(name) # Unprint to see live
    print(birthday) # Unprint to see live

    # save into data! This is how we keep the information between loops of Linux and his father.
    data.append((name, birthday))

    # open a csv file with append, so old data will not be erased
    # now, it saved row by row

with open('index.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for name, birthday in data:
        writer.writerow([name, birthday, datetime.now()])