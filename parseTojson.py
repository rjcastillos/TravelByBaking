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
CLASSES_TO_PROCESS=("wp-block-heading","has-text-align-center wp-block-post-title")
PRE="<"
POST="</"
CLOSEt=">"
TAG_SEARCH=r"<(.*?)>"
oTag=''
cTag=''
PAYLOAD_PATTERN=''
PROCESS_CLASS=False


file=open (INFILE)
Raw_Data=file.read()
lines=Raw_Data.split("\n")
file.close()
if DEBUG: print("Processing",len(lines),"lines" )
for line in lines:
    if DEBUG: 
        print("LINE:",line)
    Tag=re.findall(TAG_SEARCH, line, flags=0)
    if DEBUG:
        print("Tag Lenght ",len(Tag))
        if len(Tag)>2:
            print ("TAG > 2 ",Tag)
    
    i_tag=Tag[0]
    PROCESS_CLASS=False
    if DEBUG: print("TAG ===>",i_tag,"<== PARSED ")
    if i_tag in str(TAGS_TO_PROCESS):
        print("Processing ",i_tag)
    else:
        print ("NOT Processing TAG ",i_tag,"looking for class")
        _class=i_tag.split("=")
        if DEBUG: print("Class =",_class,"With ",len(_class),"Lenght")
        if len(_class) > 0:
            if re.search(r"class",_class[0]):
                _className=_class[1].replace("\"","")
                if DEBUG: print("Class Name ===> ",_className)
                if _className in str(CLASSES_TO_PROCESS):
                    PROCESS_CLASS=True
                else:
                    continue
            else:
                continue
        else:
            continue
    if PROCESS_CLASS:
        oTag=">"
        cTag="<"
    else:
        oTag=PRE+i_tag+CLOSEt
        cTag="</"+i_tag+CLOSEt
    
    PAYLOAD_PATTERN=oTag+"(.*?)"+cTag
    if DEBUG: print("Pattern = ",PAYLOAD_PATTERN)
    payload=re.findall(PAYLOAD_PATTERN, line, flags=0)
    print ("TAG :",oTag,"\nContent :",payload)
    print ("CLOSE TAG",cTag)
    
    
