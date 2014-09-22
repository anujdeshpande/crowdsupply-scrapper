from bs4 import BeautifulSoup
import urllib2

response=urllib2.urlopen('https://www.crowdsupply.com/revealing-hour/tah-open-ble-arduino-board')
soup = BeautifulSoup(response.read())
response.close()
print [span.text for p in soup.find_all("p", class_="pledged") for span in p.find_all("span")]
