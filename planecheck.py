import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.planecheck.com/aspsel2.asp?man=Beech&page=0')

soup = BeautifulSoup(page.content, 'html.parser')

print soup


#mylist = soup.find_all('table')
for element in mylist:
    print element.contents
