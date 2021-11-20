
def readtext():
   """Read text file and return the contents as a list of lines.
   """
   filename = input("Filename please: ")
   text = open(filename,"r")
   value = []
   for line in text:
       value.append(int(line))
   text.close()
   return value
def average(value):
    total = sum(value)
    count = len (value)
    avy = total / count
    print ("The average of the numbers in the file is: ", avy)
    return avy
value=readtext()
average(value)