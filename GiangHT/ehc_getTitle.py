import requests
from bs4 import BeautifulSoup
 
url = "https://dantri.com.vn/the-thao.htm"
 
r = requests.get(url)
 
soup = BeautifulSoup(r.content, 'html.parser')
 
temp1 = soup.select_one('div.article-wrap')

temp2 = soup.select_one('div#bai-viet')
temp3 = temp2.select_one('div.article.list')

result = temp1.select('h3.article-title') + temp3.select('h3.article-title')

print("============TITLE=============")
print(soup.title.text)
count = 0
for i in result:
    print(i.text)
    count+=1

print('\nTotal-title: ',count + 1)
   

