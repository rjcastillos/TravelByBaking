#
#Parsing file to generate a json structure
# 
# pattern = r"<Link>(.*?)</Link>"
# payload =  re.findall(pattern, line, flags=0)
# pattern2=m1+"(.*?)"+m2
# https://docs.python.org/3/library/re.html
import re
DEBUG=True
INFILE="localworking/prueba.txt"
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

file=open (INFILE)
Raw_Data=file.read()
lines=Raw_Data.split("\n")
file.close()
if DEBUG: print("Processing",len(lines),"lines" )
for line in lines:
    if DEBUG: 
        print("LINE:",line)
    Tags=re.findall(TAG_SEARCH, line, flags=0)
    if DEBUG:
        print("Tags Length ",len(Tags))
        if len(Tags)>2:
            print ("TAG > 2 ",Tags)
    
    i_tag=Tags[0]
    PROCESS_CLASS=False
    if DEBUG: print("TAG ===>",i_tag,"<== PARSED ")
    if i_tag in str(TAGS_TO_PROCESS):
        print("Processing ",i_tag)
    else:
        print ("NOT Processing TAG ",i_tag,"looking for class")
        _class=i_tag.split("=")
        if DEBUG: print("Class =",_class,"With ",len(_class),"Length")
        if len(_class) > 0:
            if re.search(r"class",_class[0]):
                _className=re.findall(r"\"(.*?)\"",_class[1],flags=0)
                if DEBUG: print("Class Name ===> ",_className)
                if _className[0] in str(CLASSES_TO_PROCESS):
                    PROCESS_CLASS=True
                else:
                    continue
            else:
                continue
        else:
            continue
    Tags_count=0
    oTag=''
    cTag=''
    if PROCESS_CLASS:
        if DEBUG: print("Tags within Class ==>",Tags)
        for Tag in Tags:
            if Tags_count < len(Tags)/2:
                oTag=oTag+Tag
            else:
                cTag=cTag+Tag
            Tags_count=Tags_count+1
        if len(oTag) > MaxLenghtOfCharacters:
            #sEnd=len(oTag)
            #bEnd=len(oTag)-MaxLenghtOfCharacters
            #oTag=oTag[bEnd:sEnd]+CLOSEt
            oTag=CLOSEt
            cTag=PRE+cTag+CLOSEt
        else:
            oTag=PRE+oTag+CLOSEt
            cTag=PRE+cTag+CLOSEt
        
    else:
        oTag=PRE+i_tag+CLOSEt
        cTag="</"+i_tag+CLOSEt
    
    PAYLOAD_PATTERN=oTag+"(.*?)"+cTag
    if DEBUG: print("Pattern = ",PAYLOAD_PATTERN)
    payload=re.findall(PAYLOAD_PATTERN, line, flags=0)
    print ("TAG :",oTag,"\nContent :",payload)
    print ("CLOSE TAG",cTag)
    
    
