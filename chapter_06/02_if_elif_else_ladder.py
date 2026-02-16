# if elif else ladder
a = int(input("enter your age: "))

if(a>=18):
    print("your are above the age of consent")
    print("good for you")

elif(a<0):
    print("your are entering an invlid nagative age  ")

elif(a==0):
    print("your are entering 0 which is not a valid age ")

else:
    print("you are below the age of consent ")


print("end of program")


# 
a=int(input("enter your age "))

if(a>=18):
    print("yes your eligible ")

else:
    print("no your not eligible")