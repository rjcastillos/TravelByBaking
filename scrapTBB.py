#
# Scraps and selects URLs for further parsing to .json foemat by html2json
# Ideally checks if it is a new URL (added since the last run)
#
from bs4 import BeautifulSoup
import requests
import re
PREVIOUSLINKS="links.txt"
CURRENTLINKS="new_links.txt"
NEWLINKS="linkstoupdate.txt"
SaveHTML=False
Links=[]
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0'}
URLPATTERN=re.compile(r'https://travelbybaking.com/', re.IGNORECASE)
url='https://travelbybaking.com/'
#url='https://travelbybaking.com/sweet-recipes/'
#url='https://travelbybaking.com/salty-recipes/'
page = requests.get(url, headers=headers)
print(page,"E =>",page.encoding)
#quit()
if SaveHTML:
    html=page.text
#print(html)
    with open('.tmp.html','w') as o:
        o.write(html)
        
soup = BeautifulSoup(page.content, "html.parser")
for a_href in soup.find_all("a", href=True):
    #print(a_href.contents)
    #print(a_href.attrs)
    #print(dir(a_href))
    #print(a_href["href"])
    if URLPATTERN.search(a_href["href"]):
        if a_href["href"] != url:
            Links.append(a_href["href"])
            print(a_href["href"])
            deepPage = requests.get(a_href["href"], headers=headers)
            deepSoup = BeautifulSoup(deepPage.content, "html.parser")
            for deepA_href in deepSoup.find_all("a", href=True):
                if URLPATTERN.search(deepA_href["href"]):
                    if deepA_href["href"] != url:
                        Links.append(deepA_href["href"])
                        print("Deep :",deepA_href["href"])
            
    
for Link in Links:
    print(Link)
    Line=Link+"\n"
    with open(CURRENTLINKS,'a') as L:
        L.write(Line)


with open(CURRENTLINKS,"r") as c:
    _Links=c.readlines()
    
with open(PREVIOUSLINKS,"r") as p:
    previouspages = p.readlines()     

newlinks=list(set(_Links)-set(previouspages))

        
for nl in newlinks:
    print(f'New page found ',nl)
    _nl=nl+"\n"
    with open(NEWLINKS,'a') as O:
        O.write(_nl)