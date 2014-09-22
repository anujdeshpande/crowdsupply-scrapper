from bs4 import BeautifulSoup
import urllib2,pprint

response=urllib2.urlopen('https://www.crowdsupply.com/revealing-hour/tah-open-ble-arduino-board/backers')
soup = BeautifulSoup(response.read())
response.close()
backers=[p.text for li in soup.find_all("li",class_="clearfix") for p in li.find_all("p") ]
for item in backers:
    print item.encode('utf-8')
