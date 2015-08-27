from bs4 import BeautifulSoup
import requests

r = requests.get('http://www.nakedcapitalism.com/2015/08/links-8815.html')
data = r.text
soup = BeautifulSoup(data, "html.parser")

for x in soup.find("div", {'class' : 'pf-content'}).find_all('a'):
    print(x['href'])
