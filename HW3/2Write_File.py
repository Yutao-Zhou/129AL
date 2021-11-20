name = str(input ("Enter Name: ")) # Asking user to give string input of their name
age = str(input ("Enter Age: ")) # Asking user to give string input of their age
print("Your name is: ", name) # Print out the name of the user
print("Your age is: ", age) # Print out the age of the user
info=[name,age] # This creat a list that have name and age
file = open ("2Write_File.txt","w") # This creat a file
for i in info: #This creat a for loop
    file.write(i)  # This write the content in the list
    file.write('\n') #This brake a new line between content
file.close() #This close the file so other program could access it