from bs4 import BeautifulSoup
import urllib.request

url =  'https://monkeypen.com/pages/free-childrens-books'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')