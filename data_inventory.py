#
#Program to grab what is needed from csv to massage and use the updater
#
# recomended to treat the stdout 
# 
import json
SaveHTML=True
DEBUG=True

TOUPDATE={}

def jSonPrint(ThisInfo):
    fData=json.dumps(ThisInfo,indent=4)
    print("....json....")
    print(fData)
    
    
with open('localworking/allRecipesData.json',"r") as ufile:
    data = json.load(ufile)
    tmn=0
    for k in data.keys():
        if len(data[k]["ThumbNails"])==0:
            tmn=tmn+1
        #Show Recipes with more than oe ThumbbNail
        if len(data[k]["ThumbNails"])>1:
            print (f'{k},{data[k]["ThumbNails"]}')
    
print(f'Total of Recipes = {len(data)}')
print(f'Without ThumbNails = {tmn}')
    #for k in data.keys():
     #   print(f'{k},{data[k]["Categories"]},{data[k]["ThumbNails"]}')


