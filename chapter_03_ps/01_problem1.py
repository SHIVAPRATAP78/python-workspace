# write a program to greet the user with his name using input function
name = input("enter your name ")
print(f"Good morning  {name}")

#example 2
name = input ("enter your name")
print ("good afternoon {name}")
#ex it will show error because we have to use f string to print the name
  
#example 3
qualification = input("enter your qualification ")
print(f"your qualification is {qualification}")

#example 4 
age = input("enter your age ")
print(f"your look like  {age}")

#example 5 - multiple inputs
firstname =input("enter your first name ")
lastname=input("enter your last name ")
print(f"namaste  {firstname} {lastname}")

#example 6 - input with arithmetic
num1 = input("enter first number ")
num2 = input("enter second number ")
print(f"sum is {int(num1) + int(num2)}")

#example 7 - input with string operations
city = input("enter your city")
country = input("enter your country")
print(f"{city} is a city in {country}")


#example 8 - input with conditional
score = input("enter your number")
if int(score) >=60:
      print(f"congradulation! you scored {score}")
else:   print(f"congradulation you scored {score }")

#example 9 - email greeting
email = input ("enter your email adress")
print(F"welcome to our newsletter! we will send updates to {email}")


#example 10 - product information
product = input("enter product name ")
price= input ("enter price ")
print(f"product name :{product}, price :{price}")

#example 11 - personal info collection
hobby = input("enter your hobby ")
print(f"that's great! {hobby}is an execelent hobby to have ")


#example 12 - calculations with input
height = input ("enter your height in , cm ")
weight =input("enter your weight in , kg")
print(f"your height is {height}cm and your weight is {weight}kg")