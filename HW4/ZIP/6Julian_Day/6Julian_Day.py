import math
def userinput():
    date=input("Please enter a date with the format DDMmmYYYY: ")
    if len(date)>9:
        date=input("Wrong format, please enter a date with the format DDMmmYYYY: ")
    return date

def Parse(date):
    l=[]
    monthdic={"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
    while True:
        try:
            l.append(int(date[0:2]))
            l.append(monthdic[date[2:5]])
            l.append(int(date[5:9]))
        except KeyError:
                userinput()
        else:
            return l
            break

def ComJulian(date): #date is of the form [day,month mumber, year]
        return math.ceil(int(365.25*(date[2]+4716))+int(30.6001*(date[1]+1))+date[0]-1524.5)

def Dweek(date): #date is of the form Julian day number
    r=(date+1.5)%7
    re={0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday"}
    return re[math.ceil(r)]
    
date=userinput()
pdate=Parse(date)
jd=ComJulian(pdate)
print(jd)
print(Dweek(jd))