#wap to find wether given user name conatin less than 10 charecter or not 

username = input("enter your name")

if(len(username)<10):
    print("your user name contains less than 10 charecters")

else:
    print("your user name contains more than or equal to 10 charecters")