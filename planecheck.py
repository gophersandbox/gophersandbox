import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.planecheck.com/aspsel2.asp?man=Beech&page=0')

soup = BeautifulSoup(page.content, 'html.parser')


mylist = soup.find_all('a')
print mylist[0]
