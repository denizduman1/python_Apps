import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar?urt=Notebook"
hmtl = requests.get(url).content
soup = BeautifulSoup(hmtl,"html.parser")
baslik = soup.find_all('h3',{'class':'productName'})
fiyat = soup.find_all('div',{'class':'proDetail'})
for i in  range(0,25):
    price = fiyat[i].ins.text.split()
    link = fiyat[i].a.get("href")
j = 1
#print(link)
for i in range(0,25): 
    print(j,"-) ",baslik[i].text.strip()," Fiyat = ",price[0],price[1])
    j += 1
    
