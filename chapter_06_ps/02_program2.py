#wap a program to find out whether student has passed or failed if it 
# requires a totoal of 40% and atleast 33% in each subject to pass assume 
# 3 subjeects and take marks as an input from the user.

marks1 = int(input("enter marks 1:"))
marks2 = int(input("enter marks 2:"))
marks3 = int(input("enter marks 3:"))

# check for total percentage 
total_percentage =(100* ( marks1 + marks2 + marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you are pass:",total_percentage)

else:
    print("you are failed:",total_percentage)