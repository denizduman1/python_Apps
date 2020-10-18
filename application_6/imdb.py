from bs4 import BeautifulSoup
import requests

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
response = requests.get(url)
html = response.content 
soup = BeautifulSoup(html,"html.parser")
liste = soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit=10)

print("Top 10 Movies")
print("-"*20)
j=1
for i in liste: 
    title = i.find("td",{"class":"titleColumn"}).find("a").string
    date = i.find("td",{"class":"titleColumn"}).find("span").string.strip("()")
    if j<=9:
        print(j,"-)",title.ljust(51),date)
    else:
        print(j,"-)",title.ljust(50),date)
    j += 1