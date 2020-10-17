import requests
import json

class Github:
    username = ""
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = 'f06a28f156f61ca77f30a4ea769af5ef4607c539' #for auth
        
    def getUser(self,username):
        self.username = username
        response = requests.get(self.api_url+"/users/"+self.username)
        return response.json()

    def getRepositories(self):
        if  self.username != "":       
            response = requests.get(self.api_url+'/users/'+self.username+'/repos')
            return response.json()
        else:
            print("Please, First go to Find User")
            return "Please, First go to Find User"
    
    def createRepositories(self,name):
        response = requests.post(self.api_url+'/user/repos?access_token='+self.token,
                      json={
                         "name": name,
                         "description": "This is your first repository",
                         "homepage": "https://github.com",
                         "private": False,
                         "has_issues": True,
                         "has_projects": True,
                         "has_wiki": True 
                      })
        return response.json()
    
git = Github()

while True:
    secim = input("1-Find User\n2-Get Repositories\n3-Create a new repository\n4-Exit\nSeçim=")
    if secim == '4':
        break
    else:
        if secim == '1':
            username = input("Enter a username = ")
            result = git.getUser(username)            
            print(f"name = {result['name']} public repos = {result['public_repos']} followers = {result['followers']}")
        elif secim == '2':
            result = git.getRepositories()
            if result != "Please, First go to Find User":
                for repo in result:
                    print(repo['name'])
        elif secim == '3':
            name = input("repository name: ")
            result = git.createRepositories(name)
            print(result)
        else:
            print("Yanlış Seçim.")