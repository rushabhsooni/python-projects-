import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
#url = 'https://www.google.com/search?q=test'
from beautifulscraper import BeautifulScraper
scraper = BeautifulScraper()
import re

#url = 'http://example.webscraping.com/view/Brazil-3'
#html = (url)

body = scraper.go("http://example.webscraping.com/view/Brazil-3")
#re.findall(r'<td class="w2p_fw">(.*?)</td>',body)
first= body.findAll(r'<td class="w2p_fw">(.*?)</td>',body)
#print (body)
#print(body.title)
print( first)
print(first)
