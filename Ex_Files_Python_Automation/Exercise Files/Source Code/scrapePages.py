# from bs4 import BeautifulSoup
# import requests
# url = 'https://scrapingclub.com/exercise/list_basic/'
# count = 1
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
# for i in items:
#     itemName = i.find('h4', class_='card-title').text.strip('\n')
#     itemPrice = i.find('h5').text
#     print('%s) Price: %s , Item Name: %s' % (count, itemPrice, itemName))
#     count = count + 1
# pagination = soup.find('ul', class_='pagination')
# pages = pagination.find_all('a', class_='page-link')
# urls = []
# for page in pages:
#     pageNum = int(page.text) if page.text.isdigit() else None
#     if pageNum != None:
#         link = page.get('href')
#         urls.append(link)
# for i in urls:
#     response = requests.get(url + i)
#     soup = BeautifulSoup(response.text, 'lxml')
#     items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
#     for i in items:
#         itemName = i.find('h4', class_='card-title').text.strip('\n')
#         itemPrice = i.find('h5').text
#         print('%s) Price: %s , Item Name: %s' % (count, itemPrice, itemName))
#         count = count + 1

# below code is only scrap data from single page
from bs4 import BeautifulSoup
import requests
url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
count = 1
for i in items:
    itemName = i.find('h4', class_='card-title').text.strip('\n')
    itemPrice = i.find('h5').text
    print('%s) Price: %s, Item Name: %s' % (count, itemPrice, itemName))
    count = count + 1

''' 
here pagination for next page data scrap with url 
second for loop is to nevigate pgae from one page to other one.
'''
pages = soup.find('ul',  class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')
for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        x = link.get('href')
        urls.append(x)

print(urls)
count = 1
for i in urls:
    newUrl = url + i
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for i in items:
        itemName = i.find('h4', class_='card-title').text.strip('\n')
        itemPrice = i.find('h5').text
        print('%s) Price: %s, Item Name: %s' % (count, itemPrice, itemName))
        count = count + 1
