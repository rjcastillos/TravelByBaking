from requests_html import HTMLSession
from bs4 import BeautifulSoup
# requests-html 2.32.3
#https://requests.readthedocs.io/projects/requests-html/en/latest/
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
SaveHTML=True
DEBUG=True

#url='https://travelbybaking.com'
#url='https://travelbybaking.com/sweet-recipes/'
#url='https://travelbybaking.com/almond-cookies/'
url='https://travelbybaking.com/apple-mousse-cake-with-greek-yoghurt/'
def h_name(url):
    s_url=url.split('/')
    hname=s_url[len(s_url)-2]
    return hname

#with open('link_test.txt','r') as Recipes_links:
    #for Link in Recipes_links:
session = HTMLSession()    
r=session.get(url)
#about = r.html.find('title,h3,p,li')
r.html.render()
#Rendered=r.html.html
#about = r.html.find('title, h3,p,li')
#
# BeatifulSoup
#
soup=BeautifulSoup(r.html.html,'html.parser')
#print(dir(html))
#html.render(scrolldown=True, sleep=1, keep_page=True)
#H=r.content
#content=soup.select('title,h3,p,li,lo')
content=soup.find_all(["title","h3","p","li","lo","ytp-title-link yt-uix-sessionlink"])


hname=h_name(url)


o="localworking/"+h_name(url)+"_soup.html"
for item in content:
    print(item)
    Line=str(item)+"\n"
    with open("localworking/renderedtosoupurl.txt",'a') as L:
        L.write(Line)
    
if DEBUG: print ("Creating file =>",o)
new_html=soup.prettify()
with open(o,'w') as H:
      H.write(new_html)