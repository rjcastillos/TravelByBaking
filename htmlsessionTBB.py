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
#url='https://travelbybaking.com/apple-mousse-cake-with-greek-yoghurt/'
def wLine(row):
    myRow=str(row)
    with open("localworking/renderedtosoupurl.txt",'a') as L:
        L.write(myRow)
def h_name(url):
    s_url=url.split('/')
    hname=s_url[len(s_url)-2]
    return hname

with open('link_test.txt','r') as Recipes_links:
    for url in Recipes_links:
        if not url.startswith("#"):
            if DEBUG: print("Making session with",url)
            session = HTMLSession() 
            r=session.get(url)
            if r.status_code == 404:
                WA="<ERROR 404> "+url+"</ERROR 404>"
                print(WA)
                wLine(WA)
                continue
            r.html.render()
            #
            # # # BeatifulSoup
            # # 
            # # #
            # 
            soup=BeautifulSoup(r.html.html,'html.parser')
            content=soup.find_all(["title","h3","p","li","lo","ytp-title-link yt-uix-sessionlink"])
            hname=h_name(url)
            Header="\n<Header>"+str(hname)+"</Header>\n"
            wLine(Header)
            for item in content:
                if DEBUG: print(item)
                Line=str(item)+"\n"
                wLine(Line)
            #writting a html backup per page    
            new_html=soup.prettify()
            o="localworking/"+h_name(url)+"_soup.html"
            if DEBUG: print ("Creating file =>",o)
            with open(o,'w') as H:
                H.write(new_html)