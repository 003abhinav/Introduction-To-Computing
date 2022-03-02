print("\n   ========================== Ques1   ==========================\n")

#Recursive function for tower of hanoi

def tower(n,curr_rod,to_rod,temp_rod):
    if n ==0:
        return
    tower(n-1,curr_rod,temp_rod,to_rod,)
    print("Moving disk",n,"from rod",curr_rod,"to rod",to_rod)
    tower(n-1,temp_rod,to_rod,curr_rod)

tower(4,'A', 'C', 'B')        



print("\n   ========================== Ques2   ==========================\n")

#creating a list to store pascal triangle values

pascal_list=[[1]]
n=int(input("Number of rows: "))

#using iteration
print("\nusing iterative: \n")
for i in range(n-1):
    if i == 0:
        print(" "*n,1)

        
    temp=[0]+ pascal_list[-1] + [0]

    for space in range(1,n-i+1):
        print(" ",end="")
    
    new_list=[]
    for add in range(len(pascal_list[-1])+1):
        
        new_list.append(temp[add]+temp[add+1])
        print(new_list[add],end=" ")
    pascal_list.append(new_list)        
    print()

#using recursion
print("\nusing recursion: \n")

i=n
def fun(n):
    if n==0:
        return
    fun(n-1)
    
    print(" "*(i-n),end='')
    
    c=1
    for col in range(1,n+1):
        print(c,end=" ")

     #using binomial coefficient   
        c= c*(n-col)//col
    print()
    
fun(n)   


print("\n   ========================== Ques3   ==========================\n")

int_1=int(input("enter integer 1: "))
int_2=int(input("enter integer 2: "))

number=[int_1,int_2]

#calculating quotient and remainder
quotient= int_1//int_2
remainder= int_1%int_2

print("\nAre quotient/remainder callable: ", callable(quotient),"/",callable(remainder))

print("\nQuotient: ",quotient,"    Remainder: ",remainder)


#conditions to check if the value is positive
if int_1 and int_2 >0 :
    print("\nvalues are non zero\n")
else:
    print("values are not non zero\n")

new_list=[4,5,6]
new_list.extend(number)
print("extended list: ",new_list,"\n")


#filtering list
filter_list=[]
for i in new_list:
    if i>4:
        filter_list.append(i)

print("Filtered list: ",filter_list,"\n")        

filter_set=set(filter_list)
print("converted list into set: ",filter_set,"\n")

#creating immutable set
immut_set=frozenset(filter_set)
print("Immutable set: ",immut_set)

#finding max value
print("\nMax value from the set: ", max(filter_set))




print("\n   ========================== Ques4   ==========================\n")

class Student:
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
        print ("Name: ",name, "\nRoll No.: ",roll_no)

        
    def __del__(self):
        print("\nobject destroyed")
    

object1 = Student("Abhinav Sharma",21104003)
del object1


print("\n   ========================== Ques5   ==========================\n")


class Database:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        print("Name: ",name,"\nSalary: ",salary,"\n")
    def __del__(self):
        print("details deleted of ",self.name)

employee_1=Database("Mehak",40000)
employee_2=Database("Ashok",50000)
employee_3=Database("Viren",60000)

employee_1.salary=70000
print("Updated salary of ",employee_1.name,": ",employee_1.salary,"\n")

del employee_3


print("\n   ========================== Ques6   ==========================\n")

def split_sort(word):
    str(word)
    word.lower()
    temp=[]
    for i in word:
        temp.append(i)
    temp.sort()
        
    return temp    
        
def friendship_game():
    print("Friendship game started\n")

    player_1=input("Enter name of player 1: ")
    print()
    player_2=input("Enter name of player 2: ")
    print()
    word_1=input("Player 1 enter your word: ")
    print()
    word_2=input("Player 2 enter your word: ")
    print()
    if split_sort(word_1) == split_sort(word_2):
        print("Friendship of ",player_1," and ",player_2," is TRUE")

    else:
        print("Friendship of ",player_1," and ",player_2," is FALSE")
    

friendship_game()
