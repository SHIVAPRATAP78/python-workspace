# a spam comment is difined as a text containing following keywords:
#make  a lot of money" .  "buy now ", "subscribe this ","click this ." wright a program to detect these spam

p1 ="make a lot of money"
p2 ="buy now"
p3 ="subscribe this"
p4 ="click this"
message = input("enter your comment")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("this comment is a spam")

else: 
    print("this comment is not a spam")
    