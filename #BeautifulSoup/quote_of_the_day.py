import requests
from bs4 import BeautifulSoup
import urllib.request

url = requests.get('https://www.brainyquote.com/quote_of_the_day')
url = url.text
soup = BeautifulSoup(url,'html.parser')

quote = soup.findAll('a',{'class': 'oncl_q'})[1].text
author = soup.find('a', {'class': 'oncl_a'}).text

print()
print()
print("\"" + quote + "\"")
print()
print("~ " + author)
print()