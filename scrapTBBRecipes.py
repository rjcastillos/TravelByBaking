from bs4 import BeautifulSoup
import requests
SaveHTML=True
DEBUG=True
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0'}
#url='https://travelbybaking.com'
#url='https://travelbybaking.com/sweet-recipes/'

with open('link_test.txt','r') as Recipes_links:
    for Link in Recipes_links:
        print (Link)
        url=Link
        n=url.split('/')
        if DEBUG: print ("n => ",n)
        RecipeName=n[len(n)-2]
        if DEBUG: print("Recipe Name => ",RecipeName)
        page = requests.get(url, headers=headers)
        if SaveHTML:
            html=page.text
            htmlname=RecipeName+".html"
            with open(htmlname,'w') as o:
                o.write(html)
        soup = BeautifulSoup(page.content, "html.parser")
        for a_href in soup.find_all("a", href=True):
            #Links.append(a_href["href"])
            print(a_href["href"])
            #for Link in Links:
             #   print(Link)
              #  Line=Link+"\n"

