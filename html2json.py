#
#Parsing html to map tags to  a json objects
# 
# 
# pattern = r"<Link>(.*?)</Link>"
# payload =  re.findall(pattern, line, flags=0)
# pattern2=m1+"(.*?)"+m2
# https://docs.python.org/3/library/re.html
from requests_html import HTMLSession
from bs4 import BeautifulSoup
# requests-html 2.32.3
#https://requests.readthedocs.io/projects/requests-html/en/latest/
import re
import json
DEBUG=False
INFILE="localworking/prueba.txt"
OUTPUTFILE="allRecipesData.json"
TAGS_TO_PROCESS=("Link","Header","title","p","li","h3")
CLASSES_TO_PROCESS=("wp-block-heading","has-text-align-center wp-block-post-title","has-text-align-center wp-block-post-title")
PRE="<"
POST="</"
CLOSEt=">"
TAG_SEARCH=r"<(.*?)>"
oTag=''
cTag=''
PAYLOAD_PATTERN=''
PROCESS_CLASS=False
MaxLenghtOfCharacters=20
Myinfo={}
allInfo={}
url="https://travelbybaking.com/almond-cookies/"

def mPrint(jLine):
    print(jLine)

def h_name(url):
    s_url=url.split('/')
    hname=s_url[len(s_url)-2]
    return hname
def jSonPrint(Myinfo):
    allInfo[Myinfo['RecipeCodeName']]=Myinfo
    fData=json.dumps(Myinfo,indent=4)
    print("....json....")
    print(fData)


##### Getting the Header / RecipeCodeName
# Always printed 
#
Header=h_name(url)
jLine='"RecipeCodeName":"'+'"'+Header+'"'
Myinfo['RecipeCodeName']=Header
mPrint(jLine)

##### Getting the Session and Rendering the page
s = HTMLSession()
r = s.get(url)

r.html.render(sleep=1)

if DEBUG:print(r.status_code)

#ShortDescription=<title>
ShortDescription=r.html.find("title" , first=True)
jLine='"ShortDescription :"'+ShortDescription.text
Myinfo['ShortDescription']=ShortDescription.text
if DEBUG : mPrint(jLine)

#Title 
Title=r.html.xpath('/html/body/div/main/div[1]/h3',first=True)
Myinfo['Title']=Title.text

#Descrpition
Description=r.html.xpath('/html/body/div/main/div[2]/p[1]',first=True)
Myinfo['Description']=Description.text

#Ingredients as a list
Myinfo['Ingredients']=[]
xIngredients=r.html.xpath('/html/body/div/main/div[2]/div/div[2]/ul')
for ulli in xIngredients:
     if DEBUG: print(ulli.text)
     Myinfo['Ingredients'].append(ulli.text)   

#Directions as a list
Myinfo['Directions']=[]
xDirections=r.html.xpath('/html/body/div/main/div[2]/div/div[3]')

if DEBUG: print("Directions type ",type(xDirections),"and length",len(xDirections))
for li in xDirections:
    if DEBUG: print(li.text)
    Myinfo['Directions'].append(li.text)

# Serving Size as a list
Myinfo['ServingSize']={}

xServingSize=r.html.xpath('/html/body/div/main/div[2]/div/div[1]/div[1]')
#print("xServingSize : len type and content ",len(xServingSize),type(xServingSize),xServingSize)
ite=0
xTxt=xServingSize[0].text
colname,ssize=xTxt.split('\n')
Myinfo['ServingSize']['colName']=str(colname)
Myinfo['ServingSize']['Size']=str(ssize)

#Time of preparation
Myinfo['rTime']=[]
xRtime=r.html.xpath('//*[@id="wp--skip-link--target"]/div[2]/div/div[1]/div[2]')
#print("xRtime : len type and content ",len(xRtime),type(xRtime),xRtime[0])
for item in xRtime:
    pieces=item.text.split('\n')
    for piece in pieces:
        Myinfo['rTime'].append(piece)

#Extracting VideoUrl
Myinfo['VideoUrl']={}
fVideoUrl=r.html.find('iframe')
print("VIDEO URL IN YT ==>")
for xv in fVideoUrl:
    if DEBUG:print(xv)
    src=xv.attrs['src']
    alt=xv.attrs['title']
    Myinfo['VideoUrl']['src']=src
    Myinfo['VideoUrl']['alt']=alt
#print("VIDEO URL IN YT ==>",VideoUrl.text)
#Myinfo['VideoUrl']=VideoUrl.text

jSonPrint(Myinfo)

with open (OUTPUTFILE,"w") as o:
    json.dump(allInfo,o)