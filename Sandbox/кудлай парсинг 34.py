from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('https://trends.rbc.ru/trends/social/64c79be19a7947562062392a?from=infinityscroll')
print(req)
html = req.read()

soup = BeautifulSoup(html, "html.parser")
print(soup)
news = soup.findAll('li', class = 'liga-news')