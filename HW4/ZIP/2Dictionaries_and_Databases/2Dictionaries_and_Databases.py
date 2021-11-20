csv=open("people.csv","r")
List=[]
def getuserinput():
    k=str(input ("Choose a key please(q to quit):"))
    while k not in List[0].keys() and k!="q":
        k=str(input ("Choose a key please(q to quit):"))
    return k
for line in csv:
    line=line.strip()
    
    sp=str.split(line,',')
    
    List.append({"Last name":sp[0],"First name":sp[1],"Favorite color":sp[2],"Favorite food":sp[3],"Favorite field of Physics":sp[4],"Most admired physicst":sp[5]})
 
print("Here are the keys:",List[0].keys())

k=getuserinput()

while k!="q":
    stringlist=[]
    for i in List:
        print()
        stringlist.append(i.get("Last name")+","+" "+i.get("First name")+": "+" "+i.get(k))
    
    for s in sorted(stringlist):
        print(s)
    k=getuserinput()