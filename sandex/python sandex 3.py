import urllib.request
import urllib.parse
import bs4
from bs4 import BeautifulSoup

import bs4 as bs
import requests

try :
	url = 'https://1337x.to/search/python/1/'
	url2 = 'https://www.google.com/search?q=test'
	#x = urllib.request.urlopen('https://www.google.com/search?q=')
	#print (x.read())
	headers = {}
	headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
	req = urllib.request.Request(url,headers=headers)
	resp = urllib.request.urlopen(req)
	respData = resp.read()
	saveFile = open('text1.txt','w')
	saveFile.write(str(respData))
	saveFile.close()
	#print(respData)
	soup = BeautifulSoup(respData, 'html.parser')
	print(soup.attribselect_re)
	#print(soup.findAll('a'))
	#print(soup.find(attrs='a'))
	#print(soup.prettify(encoding=None,formatter='minimal'))
	#print(bs.BeautifulSoup(respData,'lxml'))
	#print(bs.BeautifulSoup(respData,'html.parser'))
	#print(resp)
	#print(respData)
	print(soup.title.name)
	print(soup.title)
	print(soup.title.string)
	print(soup.title.text)
	print(soup.get_text())

	#+print(str(soup.find_all('p')))





except Exception as e:
 print(str(e))


#print(respData)

'''


def trade_spider(max_pages):
	page = 1

	while page <= max_pages:
		# 1url = 'https://thenewboston.com/search.php?type=0&sort=reputation&page==' + str(page)
		headers = {}
		headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'

		url = 'https://www.google.com/search?q=test'
		source_code = requests.get(url, allow_redirects=False, headers=headers)

		plain_text = source_code.text.encode('ascii', 'replace')

		soup = BeautifulSoup(plain_text, 'html.parser')
		print(soup)

		for link in soup.findAll('a', {'class': 'user-name'}):
			href = link.get('href')
			title = link.string
			print(href)
			print(title)
			print(soup)
		# For End
		print(soup)
		print(plain_text)

		# page += 1
		# print(txthref)
		# print(title)
		page = page + 1


# While end

trade_spider(2)

'''