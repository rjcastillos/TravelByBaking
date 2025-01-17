from requests_html import HTMLSession
from bs4 import BeautifulSoup
# requests-html 2.32.3
#https://requests.readthedocs.io/projects/requests-html/en/latest/
SaveHTML=True
DEBUG=True

#url='https://travelbybaking.com'
#url='https://travelbybaking.com/sweet-recipes/'
url='https://travelbybaking.com/almond-cookies/'
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
Rendered=r.html.html
about = r.html.find('title, h3,p,li')

#print(dir(html))
#html.render(scrolldown=True, sleep=1, keep_page=True)
#H=r.content

hname=h_name(url)
o="localworking/"+h_name(url)+".html"
for line in about:
    print(line.text)
    ln=line.text+"\n"
    with open("localworking/renderedurl.txt",'a') as L:
        L.write(ln)

with open(o,'w') as H:
       H.write(Rendered)