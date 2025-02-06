#
#Parsing html to map tags to  a json objects
# 
# 
# pattern = r"<Link>(.*?)</Link>"
# payload =  re.findall(pattern, line, flags=0)
# pattern2=m1+"(.*?)"+m2
# https://docs.python.org/3/library/re.html
from requests_html import HTMLSession
# requests-html 2.32.3
#https://requests.readthedocs.io/projects/requests-html/en/latest/
#
import json
DEBUG=False
LINKSTOPROCESS="linkstoupdate.txt"
OUTPUTFILE="newallRecipesData.json"
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
def jSonPrint(ThisInfo):
    fData=json.dumps(ThisInfo,indent=4)
    print("....json....")
    print(fData)
try:
    with open(OUTPUTFILE,"r") as ufile:
        allInfo = json.load(ufile)
except:
    print("File ",OUTPUTFILE," Does not exist, will be created")

with open(LINKSTOPROCESS,'r') as Recipes_links:
    for _line in Recipes_links:
        if not _line.startswith("#"):
            url=_line.replace("\n","")
            ##### Getting the Header / RecipeCodeName
            # Always printed 
            #
            Header=h_name(url)
            jLine='"RecipeCodeName":'+'"'+Header+'"'
            Myinfo['RecipeCodeName']=Header
            allInfo[Header]={}
            allInfo[Header]['RecipeCodeName']=Header
            mPrint(jLine)

            ##### Getting the Session and Rendering the page
            s = HTMLSession()
            r = s.get(url)

            r.html.render(sleep=1)

            if DEBUG:print(r.status_code)
            #Link
            Myinfo["Link"]=url
            allInfo[Header]["Link"]=url
            #ShortDescription=<title>
            ShortDescription=r.html.find("title" , first=True)
            jLine='"ShortDescription :"'+ShortDescription.text
            Myinfo['ShortDescription']=ShortDescription.text
            allInfo[Header]['ShortDescription']=ShortDescription.text
            if DEBUG : mPrint(jLine)

            #Title 
            Title=r.html.xpath('/html/body/div/main/div[1]/h3',first=True)
            Myinfo['Title']=Title.text
            allInfo[Header]['Title']=Title.text

            #Descrpition
            Myinfo['Description']=''
            allInfo[Header]['Description']=''
            
            Description=r.html.xpath('/html/body/div/main/div[2]',first=False)

        
            if Description:
                for _Des in Description:
                    Myinfo['Description']=Myinfo['Description']+(_Des.text)
                    allInfo[Header]['Description']=allInfo[Header]['Description']+(_Des.text)
            else:
                Myinfo['Description']="CHECK DESCRIPTION @"+url
                allInfo[Header]['Description']="CHECK DESCRIPTION @"+url

            #Ingredients as a list
            Myinfo['Ingredients']=[]
            allInfo[Header]['Ingredients']=[]
            xIngredients=r.html.xpath('/html/body/div/main/div[2]/div/div[2]/ul')
            #
            #xIngredients=r.html.find('.wp-block-ryelle-recipe-ingredients',first=False)
            #
            #https://requests.readthedocs.io/projects/requests-html/en/latest/
            #
            for ulli in xIngredients:
                if DEBUG: print(ulli.text)
                Myinfo['Ingredients'].append(ulli.text)
                allInfo[Header]['Ingredients'].append(ulli.text)   

            #Directions as a list
            Myinfo['Directions']=[]
            allInfo[Header]['Directions']=[]
            xDirections=r.html.xpath('/html/body/div/main/div[2]/div/div[3]')

            if DEBUG: print("Directions type ",type(xDirections),"and length",len(xDirections))
            for li in xDirections:
                if DEBUG: print(li.text)
                Myinfo['Directions'].append(li.text)
                allInfo[Header]['Directions'].append(li.text)

            # Serving Size as a list
            Myinfo['ServingSize']={}
            allInfo[Header]['ServingSize']={}

            xServingSize=r.html.xpath('/html/body/div/main/div[2]/div/div[1]/div[1]')
            #print("xServingSize : len type and content ",len(xServingSize),type(xServingSize),xServingSize)
            ite=0
            try:
                xTxt=xServingSize[0].text
                colname,ssize=xTxt.split('\n')
            except:
                colname="NA"
                ssize="NA"
            Myinfo['ServingSize']['colName']=str(colname)
            allInfo[Header]['ServingSize']['colName']=str(colname)
            Myinfo['ServingSize']['Size']=str(ssize)
            allInfo[Header]['ServingSize']['Size']=str(ssize)

            #Time of preparation
            Myinfo['rTime']=[]
            allInfo[Header]['rTime']=[]
            xRtime=r.html.xpath('//*[@id="wp--skip-link--target"]/div[2]/div/div[1]/div[2]')
            #print("xRtime : len type and content ",len(xRtime),type(xRtime),xRtime[0])
            for item in xRtime:
                pieces=item.text.split('\n')
                for piece in pieces:
                    Myinfo['rTime'].append(piece)
                    allInfo[Header]['rTime'].append(piece)

            #Extracting VideoUrl
            Myinfo['VideoUrl']={}
            allInfo[Header]['VideoUrl']={}
            fVideoUrl=r.html.find('iframe')
            if DEBUG: print("VIDEO URL IN YT ==>")
            for xv in fVideoUrl:
                if DEBUG:print(xv)
                src=xv.attrs['src']
                alt=xv.attrs['title']
                Myinfo['VideoUrl']['src']=src
                allInfo[Header]['VideoUrl']['src']=src
                Myinfo['VideoUrl']['alt']=alt
                allInfo[Header]['VideoUrl']['alt']=alt
            #print("VIDEO URL IN YT ==>",VideoUrl.text)
            #Myinfo['VideoUrl']=VideoUrl.text
    

            
            jSonPrint(Myinfo)

with open (OUTPUTFILE,"w") as o:
    json.dump(allInfo,o)