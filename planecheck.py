import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.planecheck.com/aspsel2.asp?man=Beech&page=0')

soup = BeautifulSoup(page.content)


mylist = soup.find_all('div')
print mylist[0]
