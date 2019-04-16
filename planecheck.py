import argparse
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("environment")
args = parser.parse_args()

if args.echo == 'production':
  page = requests.get('http://www.planecheck.com/aspsel2.asp?man=Beech&page=0')
  soup = BeautifulSoup(page.content, 'html.parser')
elif args.echo == 'development':
  page = open('test/testpage.html')
  soup = BeautifulSoup(page.content, 'html.parser')
  page.close()

mylist = soup.find_all('div')
print mylist[0]
