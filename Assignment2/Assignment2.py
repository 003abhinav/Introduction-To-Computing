print("  ========================== Ques1   ==========================\n")
string = "Python is a case sensitive language\n"
print("String: ",string)

#finding length of the string
print("Length of the string: ",len(string))

#reversing string
print("\nReversing the string: ",string[-1::-1])

#slicing string
print("\nSlicing: ",string[10:26])

#replacing string
print("\nReplacing string: ",string.replace("a case sensitive","object oriented"))

#finding index
print("\nIndex of 'a': ",string.find("a"))

#removing white space
print("\nRemoving white spaces: ",string.replace(" ",""))

print("\n  ========================== Ques2  ==========================\n")

#storing student information in a list
list= ["Abhinav Sharma", "21104003","Electrical", "9.9"]
print("Student Data: ",list,"\n")

#using multiline string 
print('''Hey, ''',list[0],''' Here!
My SID is ''',list[1],'''
I am from ''',list[2],''' department and my CGPA is ''',list[3])

print("\n  ========================== Ques3  ==========================\n")

a=56
b=10

print("a:",a,", b:",b,"\n")
print("a&b: ",a&b) # "and" operator
print("a|b: ",a|b) # "or" operator
print("a^b: ",a^b) # "xor" operator
print("\nLeft shifting 'a' with 2 bits: ", a<<2,"\nLeft shifting 'b' with 2 bits: ",b<<2) #left shifting
print("\nRight shifting 'a' with 2 bits: ",a>>2, "\nRight shifting 'b' with 4 bits: ",b>>4) #right shifting


print("\n  ========================== Ques4  ==========================\n")

i=0                       #initializing variable for while loop
number= []                #creating an empty list to store users input
greatest=0                #variable to store the greatest input

while i<3:
    number.append(int(input("Enter any number \n")))      #storing value in number list
    if number[i] >= greatest:                             #comparing the numbers
        greatest=number[i]                                #storing the greater value
    i+=1
    
print("Greatest number entered by the user ", greatest)

print("\n  ========================== Ques5  ==========================\n")

#taking input
string= input("enter any string\n")

#checking if the string contains "name"
if string.find("name") != -1:
    print("Yes, it contains 'name'")
else:
    print("No, it does not contains 'name'")

print("\n  ========================== Ques6  ==========================\n")

i=0                    #variable for while loop
triangle=[]            #creating an empty list for input
while i<3:
    i+=1
    triangle.append(int(input("enter the value of side of triangle\n")))    #storing values in the list
triangle.sort()                                                             #sorting the list to get the longest side, another way to do ques4

#using the sides test
if triangle[0]+triangle[1] >= triangle[2]: 
    print("Yes, triangle can be formed by these sides")
else:
    print("No, triangle can't be formed by these sides")
    
