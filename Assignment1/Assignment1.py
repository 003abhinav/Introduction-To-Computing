#Ques 1
#Average of three numbers

#Taking input from the user
print("  ========================== Ques1   ==========================\n")
number1= input("enter a number: ")
number2= input("enter another number: ")
number3= input("enter another number: ")

average= (int(number1)+int(number2)+int(number3))/3 #converting str to int and taking average

print('The average of the given number: ', average)

#Ques 2

#Calculating tax
print("\n  ========================== Ques2  ==========================\n")
tax_rate= 0.20
standard_deduction= 10000
dependent_deduction= 3000

gross_income= input("Gross Income: ")
total_dependents= input("Number of dependents: ")

taxable_income= int(gross_income) - standard_deduction - (dependent_deduction * int(total_dependents))

tax= taxable_income * tax_rate
print("Taxable Income: ", taxable_income,"$")
print("Your tax: ", tax, "$")

#Ques 3

#Storing different data types in a list
print("\n  ========================== Ques3  ==========================\n")
sid= int(input("SID: "))
name= input("Name: ")
gender= input("Gender: ")
course= input("Course: ")
cgpa= float(input("CGPA: "))

student= [sid,name,gender,course,cgpa]
print(student)

#Ques 4

#Storing marks in a list and sorting them
print("\n  ========================== Ques4  ==========================\n")
marks= [30,25,22,40,20]
print("List before sorting: ",marks)
marks.sort()
print("List after sorting",marks)

#Ques 5
print("\n  ========================== Ques5  ==========================\n")
#Deleting and replacing items in a list
color1= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color2= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

print("Default list: ",color1)
#deleting item from a list
del color1[3]
print("\nDeleting 'Black' from the list:  ",color1)

#replacing items from a list
color2[3:5]= ['Purple','Purple']
print("\nReplacing 'Black' & 'Pink' with 'Purple' int the list:\n",color2)

