#
#Parsing file to generate a json structure
# 
# pattern = r"<Link>(.*?)</Link>"
# payload =  re.findall(pattern, line, flags=0)
# pattern2=m1+"(.*?)"+m2
# https://docs.python.org/3/library/re.html

DEBUG=True
INFILE="localworking/prueba.txt"
TAGS_TO_PROCESS=("Link","Header","title","p","li","h3")
PRE="<"
POST="/>"



file=open (INFILE)
Raw_Data=file.read()
lines=Raw_Data.split("\n")
if DEBUG: print("Processing",len(lines),"lines" )
for line in lines:
    Tag=line.split('>')
    i_tag=Tag[0].replace("<","")
    if DEBUG: print("TAG ===>",i_tag,"<== PARSED ")
    if i_tag in str(TAGS_TO_PROCESS):
        print("Processing ",i_tag)
    else:
        print ("NOT Processing")
    sufix="</"+i_tag
    payload=Tag[len(Tag)-2].replace(sufix,"")
    print ("TAG :",i_tag,"\nContent :",payload)
    
    
