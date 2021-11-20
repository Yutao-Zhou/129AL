string = str(input ("String with at least 3 words: "))

def input_check(string):
    while True:
        global s
        s=str.split(string)
        if len(s)<3:
            string = str(input ("String with at least 3 words:"))
        else:
            print(*s,sep='\n')
            break
input_check(string)
print("First 3 Characters:",string[:3])
print("Last 3 Characters:",string[-3:])
n=int((len(string)+1)/2)
print("First half of the string:",string[:n])
print("Last half of the string:",string[-n:])
reversed_words = reversed(s)
reverse_sentence = ' '.join(reversed_words)
print("Reversed words:",reverse_sentence)
alf=' '.join(sorted(s))
print("Alphabetized words",alf)
for character in string:
    print (character)
for character in string: 
    print(hex(ord(character)))