import requests
import json

class TheMovies:
    def __init__(self):
        self.apiURL  = "https://api.themoviedb.org/3/"
        self.apiKEY = "047f3af5d582a0f4779acb2ac5909e03"
        
    
    def getPopulars(self):
        response = requests.get(self.apiURL+"movie/popular?api_key="+self.apiKEY+"&language=en-US&page=1")
        return response.json()
    
    def getSearch(self,keyword):
        response = requests.get(self.apiURL+"search/company?api_key="+self.apiKEY+"&query="+keyword+"&page=1")
        return response.json()
    
thm = TheMovies()

while True:
    secim = input("\n1-Popular Movies\n2-Search Movies\n3-Exit\nEnter = ")
    if secim == '3':
        break
    else:
        if secim=='1':
            movies = thm.getPopulars()
            # i=0
            # popular = {}}
            # while i<20:
            #     popular.append(movies['results'][i]['vote_average'])
            #     i=i+1
            # popular.sort()
            # popular.reverse()
            # for i in popular:
            for movie in movies['results']:
                print(movie['title'])
            print("-"*50)
        elif secim == '2':
            i = 1
            search = input("Search = ")
            searchs = thm.getSearch(search)
            for movie in searchs['results']:
                print(i,"-) ",movie['name'])
                i = i + 1
            print("-"*50)
