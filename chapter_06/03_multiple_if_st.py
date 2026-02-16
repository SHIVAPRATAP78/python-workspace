a = int(input("enter your age: "))

#if statment no:1
if(a%2 == 0):
    print("a is even ")
#end of if statment no:1


#if statment no:2
if(a>=18):
    print("your are above the age of consent")
    print("good for you")


elif(a<0):
    print("your are entering an invlid nagative age  ")

elif(a==0):
    print("your are entering 0 which is not a valid age ")
 # end of if statment n0:2
else:
    print("you are below the age of consent ")


print("end of program")