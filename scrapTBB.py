from bs4 import BeautifulSoup
import requests
SaveHTML=False
Links=[]
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0'}
#url='https://travelbybaking.com'
#url='https://travelbybaking.com/sweet-recipes/'
url='https://travelbybaking.com/salty-recipes/'
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
    Links.append(a_href["href"])
    #print(a_href["href"])
    
for Link in Links:
    print(Link)
    Line=Link+"\n"
    with open('links.txt','a') as L:
        L.write(Line)
