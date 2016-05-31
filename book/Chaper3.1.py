import requests
from bs4 import BeautifulSoup
import re
import datetime
import random

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    titleUrl = 'http://en.wikipedia.org'
    wb_data = requests.get(titleUrl + articleUrl)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    return soup.find('div', {'id' : 'bodyContent'}).findAll('a', href = re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
print("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)


