# case conversion
# lower() | upper() | title() | capitalize()

# cleaning the string 
# strip() | lstrip() | rstrip()

#serching and counting in the string
# find() | index() | count() | startswith() | endswith()

#to modify the string/ /  split and join
# replace() | split() | join() | strip()

#




name = "pratap" 

print(len(name)) # it will give the length of the string

print(name.endswith("p")) # it will check the last charecter of the string if it is "p" then it will return true otherwise false
print(name.startswith("p")) # it will check the first charecter of the string if it is "p" then it will return true otherwise false

print(name.capitalize()) #its just capitalise the first letter of the string

print(name.upper() ) # it will capitalise the whole string

print(name.lower()) # it will convert the whole string into lower case

name="pratap talwar is a python devolper"
print(name.title()) # it will capitalise the first letter of each word in the 

#searching and counting in the string

name ="python"
print(name.find("o")) # it will give the index of the first occurrence of the charecter "o" in the string
print(name.find("t")) # it will give the index of the first occurrence of the charecter "t" in the string
print(name.find("a")) # it will give -1 because there is no "a"

name ="shiva pratap"
print(name.count("a")) # it will count the number of "a" in the string
print(name.count("s")) # it will count the number of "s" in the string
print(name.count("p")) # it will count the number of "p" in the string

name = "spider man"
print(name.endswith("n")) # it will check the last charecter of the string if it is "n" then it will return true otherwise false
print(name.startswith("s")) # it will check the first charecter of the string if it is "s" then it will return true otherwise false

#replacing and modifying the string

a = "batman"
print(a.replace("b",("r"))) # it will replace the first occurrence of "r" with "b" in the string
print(a.replace("batman","superman")) # it will replace the whole string "batman" with "superman"
print(a.replace("a","o")) # it will replace all the occurrence of "a" with "o" in the string

print(a.replace(" ","-")) # it will replace the space with "-" in the string

string=" i like java "
print(string.replace("java","python")) # it will replace "java" with "python" in the string


# splitting and joining the string
name = "pratap talwar"
print(name.split()) # it will split the string into a list of words
name = "batman is a super hero and he is so strong "
print(name.split()) # it will split the string into a list of words

# joining the string
name =["captain","america","is","a","super","hero"]
print(" ".join(name)) # it will join the list of words into a string without any space

# striping the string

name ="   python devolper   "
print(name.strip()) # it will remove the leading and trailing spaces from the string

#find vs index
name = "pratap"
print(name.find("t")) # it will give the index of the first occurrence of "p" in the string
print(name.index("p")) # it will give the index of the first occurrence of "p" in the string

# if the character is not found, find() returns -1 but index() raises an error
print(name.find("z")) # it will return -1 because there is no "z"
# print(name.index("z")) # this would raise an error because there is no "z"



# string formatting
name = "pratap"
age = 25
print("my name is {} and my age is {}".format(name,age)) # it will format the string by replacing the {} with the values of name and age

a = "this is test. this is easy."
print(a.find("is"))

string = " python is fun .fun is python"
reversd_string = "".join(reversed(string)) # it will reverse the string but it will return a reversed object which is not a string
print(reversd_string)# it will reverse the string but it will return a reversed object which is not a string    


s = "python"
reversed_s = "".join(reversed(s))
print(reversed_s)

#revers word order in a string
s = "bat man is richest man in the world"
print(" ".join(s.split()[::-1])) # it will split the string into a list of words and then reverse the list and then join the list into a string with space in between


