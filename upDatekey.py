import json
with open('localworking/Directionstofix.json', 'r') as f:
	updatesList = json.load(f)


for idx, xDict in enumerate(updatesList):
    print("Iteration :",idx)
    for k,v in xDict.items():
        print("Update Key",k, "with new value ",v[:20])
