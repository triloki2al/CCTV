# #name="Vipin"
# #Age=21
# #Address="Noida"
# #print("My Name is",name)
# #print("My age",Age)
# #print("My Adreess",Address)

# #a=1000
# #b=500
# #sum=a+b
# #print(sum)

# a=10
# b=30
# print(a+b)
# print(a-b)
# print(a*b)
# print(b/a) 
# print(a%b)
# print(a**b)

# print(a==b)
# print(a!=b)
# print(a>=b)
# print(b<=a)

# num=10
# #num=num+10
# #num+=10
# #num-+5
# #num*=10
# num/=10
# print("Number",num)

# #logical operator
# print(not True)
# print(not False)

# a=50
# b=30
# print(not (a>b))

# #val1=False
# #val2=True
# #print("AND Operator", val1 and val2)
# #print("OR Operator",val1 or val2)
# #print("OR", (a==b) or (a>b))

# #type conversion
# #a=int("2")
# #b=4.5
# #print(type(a))
# #print(a+b)

# #type casting

# name=input("Plase Enter you name")
# print(name)
# age=int(input("Please Enter your age"))
# print(type(age))
# print(age)
# marks=input("Please enter your marks")
# print(marks)

# firstnum=int(input("Input your first Number"))
# secondnum=int(input("Input your second Number"))
# sum=firstnum+secondnum
# print(sum)

# a=input("Input your first number")
# b=input("Input your second number")

# print(a>=b)

#concanate function
# a="My Compnay name is Fortune, \n Our brand name Secureye"
# b="My Compnay name is Fortune, \t Our brand name Secureye"
# print(a)
# print(b)

# str1="Live Pro"
# str2="Secureye"
# str_re=str2+" "+str1
# str3=str1[2]
# print(str_re)
# print(str3)

# str1="noida Uttar Pradesh"
# print(str1[5:len(str1)])
# print(str1.endswith("esh"))
# print(str1.capitalize())
# print(str1.replace("a","T"))

# #First Example
# inputfirstname=input("Enter you first Name:")
# print(len(inputfirstname))

# #second Example
# str="My name is $ and location is $"
# print(str.count("$"))

#IF elif else

# age=22
# if(age>=18):
#     print("He can vote")

#Light Example
# light="pink"
# if(light=="Red"):
#     print("STOP")
# elif(light=="Green"):
#     print("GO")
# elif(light=="Orange"):
#     print("Look and GO")
# else:
#     print("Light not working")

# print("End of Code")

#Vote Example
# age=16
# if(age>=18):
#     print("he can Vote")
# else:
#     print("Can not Vode")

#Example of Grade System
# mark=int(input("Input your marks"))
# if(mark>=90):
#     print("Grade : A")
# elif(mark>=80 and mark<90):
#     print("Grade: B")
# elif(mark>=70 and mark<80):
#     print("Grade C")
# else:
#     print("Your are Fail")
# print("End of Code")


# #Nested If
# age=95
# if(age>=18):
#     if(age>80):
#         print("Can not drive")
    
# else:
#     print("can not drive")

#Example of ODD and Even Number
# num=int(input("Enter your number"))
# rem=num % 2
# if(rem==0):
#     print("Even")
# else:
#     print("ODD")

#list=[12,15,18,50,60]
#list.sort()
#list.short(reverse=True)
#list.append(80)
# print(list)
# list.insert(1,100)
# list.pop(5)
# print(list)

# #While Loop Example
# count =1
# while count <=5:
#     print("Hello")
#     count +=1

# i=5
# while i>=1:
#     print(i)
#     i-=1


# print("end of while loop")
# i = 1
# while(i <=100):
#     print(i)
#     i += 1


# print("end of while loop")    

# i = 100
# while (i >=1):
#     print(i)
#     i -=1
# print("while loop end")


# n =int(input("Enter you number"))
# i = 1
# while (i <=10):
#     print(n*i)
#     i += 1

# num = [10,12,56,88,10]
# idx = 0
# while idx > len(num):
#     print(num[idx])
# idx += 1

# nums = ["T", "S", "J"]
# idx =0
# while idx <len(nums):
#     print(nums[idx])
#     idx += 1

# num = (10,12,56,88,10,36)

# x = 36
# idx=0
# while idx < len(num):
#     #print(num[idx])
#     if(num[idx] == x):
#         print("found x value",x)
#         if(idx ==x):
#         break
#     else:
#         ("not found")
#     idx += 1

#Break statement


# i = 0
# while i <= 5:
#     print(i)
#     if(i == 3):
#         break
#     i += 1
#     print("end of loop")

# num1= [55,66,88,21,66]
# for el in num1:
#     print(el)



# num1= [55,66,88,21,66]
# for el in num1:
#     if (el ==66):
#         print("66 found")
#     print(el)


# for i in range(1, 101):
#         print(i)

# for el in range(100,0, -1):
#     print(el)

#FUNCATION

# def cal_sum(a, b):
#     return a+b
# sum=cal_sum(10,20)
# print(sum)

# def cal_fac(n):
#     fact=1
#     for i in range(1,n+1):
#         fact *=i
#         print(fact)

# def convertor(usd_val):
#     inr_val=usd_val * 83
#     print(usd_val,"USD", inr_val, "INR")

# convertor(73)    

#recursing function
# def show(n):
#     if(n ==0):#base case
#         return
#     print(n)
#     show(n - 1)
#     print("END")

# show(4)    

# class Student:
#     collagename="ApnaCollage"

#     def __init__(self, name, marks):
#         self.name=name
#         self.marks=marks

#     def welcome(self):
#         print("Wel Come Student", self.name)

#     def get_marks(self):
#         return self.marks


# s1 = Student("Karna", 97)
# s1.welcome()
# print(s1.get_marks())

# class Employee:

#     def __init__(self, name, marks):
#         self.name = name
#         self.mark =marks

#     def getresult(self):
#         return self.mark

# e1 = Employee("Rohit", 98)
# e1.getresult()
# print(e1.getresult())


# class Student:
#     def Studentdata(self, name, age, marks):
#         name = input("Enter your Name")
#         self =self
#         age = int(input("Input your Age"))
#         age =age
#         marks = int(input("Input your Marks"))
#         marks =marks
#         if(marks >=1):
#             print("Marks is Valid")
#         else:
#              print("Marks is Invalid, Please enter valid marks")
# st =Student()
# st.Studentdata(name="ram",marks=44, age=23)

# age = int(input("Enter you age"))
# if age >= 18:
#     print("Yes")
# else:
#     print("No")


with open('sample.txt', 'w') as f:
    f.write('hello cctv how are you')
    f.write("I am adding text")
    f.close





