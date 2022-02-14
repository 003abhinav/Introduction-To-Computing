print("\n   ========================== Ques1   ==========================\n")

#taking input from the user and lowercasing
string= input("Enter any string: ")
string= string.lower()

#checking if the user input is a string or a single word
if len(string.split(" ")) == 1:
    for i in string:
        print(i,":",string.count(i))    #counting in case of single word
else:
    for i in string.split(" "):
        print(i,":", string.count(i))   #counting in case of string
    


    
print("\n   ========================== Ques2   ==========================\n")


#function to take input from the user
def user_input():
    global date
    date={}
    inp= ["Day", "Month","Year"]
    for i in inp:
        date[i]= int(input(i + ": "))
        
user_input()

#list of months with 31 days
months1=[1,3,5,7,8,10,12]

#list of months with 30 days
months2=[4,6,9,11]

#function to print the date
def print_date():
    print("Next Date is: ",date["Day"],"/",date["Month"],"/",date["Year"])

def invalid_input():
    print("enter a valid date")

def next_month():
    date["Month"] += 1
    date["Day"]=1
    
#condition to check if the input is valid
if date["Month"] >12 or date["Month"]<=0 or date["Day"] >31 or date["Day"]<=0 or date["Year"]<=0:
        invalid_input()

#condition for the new year
elif date["Month"]==12 and date["Day"]==31:
    date["Year"] += 1
    date["Month"] = 1
    date["Day"] = 1
    print_date()

#condition to change the month        
elif date["Month"] in months1 and date["Day"]==31:
    next_month()
    print_date()

#condition to change the month 
elif date["Month"] in months2 and date["Day"]==30:
    next_month()
    print_date()

#condition for leap year
elif date["Year"]%4==0 and date["Day"]==28:
    date["Day"] += 1
    print_date()    

#condition for feburary
elif date["Month"]==2 and date["Day"]==28:
    next_month()
    print_date()    

#condition for leap year
elif date["Year"]%4==0 and date["Month"]==2 and date["Day"]==29:
     next_month()
     print_date()

#conditions for inavlid input
elif (date["Month"]==2 and date["Day"]>28) or (date["Month"] in months1 and date["Day"]>31) or (date["Month"] in months2 and date["Day"]>30):
    invalid_input()
    
else:
    date["Day"] += 1
    print_date()




    
print("\n   ========================== Ques3   ==========================\n")      


#empty list to store user input
user_list=[]

#function to take input from user
def user_input():
    n=input("\nDo you want to add number to the list? (Y/N): ")
    n.lower()
    if n=="y":
       user_list.append(int(input("\nEnter the element of the string: ")))
       user_input()

user_input()

#creating a new list to store list of tuples
new_list=[]

#function for creating tuple
def create_tuple():
    for i in user_list:
       L1=[i,i**2]
       
       T1=tuple(L1)
       
       new_list.append(T1)
       
create_tuple()
print("\nlist of tuples with square: ",new_list)




print("\n   ========================== Ques4   ==========================\n")

#taking input from the user
grade=int(input("enter your grade: "))

#condition for error
if grade not in range(4,11):
    print("Error")
   
    
else :
    #function for telling grade and performance
    def grading(grade):
        list_index=grade-4
        L1=['D', 'C', 'C+', 'B', 'B+', 'A', 'A+']
        L2=['Poor', 'Below Average', 'Average', 'Good', 'Very Good', 'Excellent', 'Outstanding']
        print("\nYour Grade is '",L1[list_index],"' and ",L2[list_index], "Performance")
        
grading(grade)




print("\n   ========================== Ques5   ==========================\n")

#for loop for rows
for row in range(6,0,-1):

    #for loop for giving space
    for space in range (6-row,0,-1):
        print(" ",end="")
    #for loop for columns   
    for column in range (2*row-1):
        #converting ascii value to chr
        print(chr(65+column),end="")
        
    print()




print("\n   ========================== Ques6   ==========================\n")

#empty dictionary to store user input
student_dict={}
stop_program = False

#function to take input from the user
def student_info():
    initial=input("\nDo you want to add a student detail?(Y/N): ")
    print()
    initial=initial.lower()
    
    
    if initial == "y":
        student_name=input("Student's name: ")
        student_sid=input("Enter your SID: ")
        student_dict[student_sid]=student_name
        
        student_info()
        

    elif initial != "n":
        global stop_program
        stop_program = True
        print("Enter only y/n")

student_info()


if stop_program!= True:
    print("\nStudent details: ",student_dict,"\n")

    #storing keys in a list
    new_keys=list(student_dict)

    #storing values in a list
    new_values=list(student_dict.values())

    #sorting name in list
    sort_name=sorted(new_values)

    #empty dictionary to store data sorted by name
    sort_name_dict={}

    #sorting SID
    sort_keys=sorted(new_keys)

    #empty dictionary to store data sorted by sid
    sort_keys_dict={}


    for i in range(len(sort_name)):

        #finding index of sorted name in original dictionary
        name_index=sort_name.index(new_values[i])

        #adding elements in dictionary sorted by name
        sort_name_dict[new_keys[name_index]]=sort_name[i]

    print("Sorting by names: ",sort_name_dict,"\n")


    for i in range(len(sort_keys)):
        
        #finding index of sorted sid in original dictionary
        keys_index=new_keys.index(sort_keys[i])

        #adding elements in dictionary sorted by sid
        sort_keys_dict[sort_keys[i]]=new_values[keys_index]

    print("Sorting by SID: ",sort_keys_dict,"\n")

    student_sid= input("Enter the SID of the student: ")

    if student_sid in new_keys:
        print("\nName of the student: '", student_dict[student_sid],"'")
        
    else :
        print("SID not found")




print("\n   ========================== Ques7   ==========================\n")

#number of terms in the sequence
n_term=int(input("Enter the total terms of the fibonacci series: "))
print()

#empty list to store sequence
fibonacci=[]

#first term of the sequence
a1=0

#second term of th sequence
a2=1

for i in range(n_term):
    if i<2:
        print(i)
        fibonacci.append(i)

    
    else:
        a_n= a1+a2
        fibonacci.append(a_n)
        print(a_n)

        
        a1=a2
        a2=a_n

average= sum(fibonacci)/len(fibonacci)     
print("\nAverage of series: ", average)




print("\n   ========================== Ques8   ==========================\n")

set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}

#all elements that are in Set1 and Set2 but not both
set_a=set1^set2
print("part a: ",set_a,"\n")

#one of the three sets Set1,Set2 and Set3
set_b=set1^set2^set3
print("part b: ",set_b,"\n")

#exactly two of the sets Set1, Set2 and Set3
set_c = (set1&set2)|(set2&set3)|(set1&set3)-(set1&set2&set3)-(set1&set2&set3)-(set1&set2&set3)
print("part c: ",set_c,"\n")


new_set=set()
for i in range(1,11):
    new_set.add(i)

#all integers in the range 1 to 10 that are not in Set1
set_d= new_set - set1
print("part d: ",set_d,"\n")

#all integers in the range 1 to 10 that are not in Set1,Set2 and Set3
set_e= new_set-set1-set2-set3
print("part e: ",set_e,"\n")
