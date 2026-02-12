# propertis of python dictioneris 
#it is unorderd
#it is mutable 
#it is indexed
#cannot contain duplicate key 

marks = {
    "pratap":100,
    "omkar":67,
    "vivek":76,
    "channu":89,
    0 : "pratap"
}

print(marks.items())

#dot keys  and values 
marks = {
    "pratap":100,
    "omkar":67,
    "vivek":76,
    "channu":89,
    0 : "pratap"
}

print(marks.keys())
print(marks.values())

#update ({"marks"}) method 
marks ={
    "partha":98,
    "omkar":89,
    "channu":78,
    "vivek":86,
    0:"partha"
}
print(marks.values())
marks.update({"partha":97,"swamy":100})
print(marks) 

# get method ("name ")
marks ={
    "partha":98,
    "omkar":89,
    "channu":78,
    "vivek":86,
    0:"partha"
}
print(marks.get("pratha"))# its prints a 'none' when we use gte method 
print(marks["partha2"]) # its returns a error 

# creating dictioners 
person= {
    "name":"partha",
    "age" : 24,
    "city": "benglore"
    } 

print(person.get("name")) #"partha"
print(person.get("salery")) # none 
print(person.get("name ",0)) #defoult value 

print(person.keys())
print(list(person.keys()))
print(person.values)



# keys and values 
marks = {
    "partha":98,
    "omkar":89,
    "channu":78,
    "vivek":86,
    0:"partha"
}
print(marks.keys())
print(marks.values())

# items  key value pair 
marks = {
    "partha":98,
    "omkar":89,
    "channu":78,
    "vivek":86,
    0:"partha"
}

print(marks.items())


# loop example 
marks = {
    "partha":98,
    "omkar":89,
    "channu":78,
    "vivek":86,
    0:"partha"
}
for keys, values in marks.items():
 print (keys,values )



#  update dictionry 
marks = {
    "name ":"pratap",
    "age":24,
    "work ":"devolepr ",
    "city ":"bengalore ",
   
}

print(marks.update({"salery":30000 ,"age":25,}))
print(marks)


# pop item removes last insertd item 
marks = {
    "name ":"pratap",
    "age":24,
    "work ":"devolepr ",
    "city ":"bengalore ",
   
}
marks.popitem()
print(marks)

# pop remove a selected key 
person= {
    "name ":"pratap",
    "age":24,
    "work ":"devolepr ",
    "city ":"bengalore ",
   
}

person.pop("age")
print(person)

#  clear () removes all the keys {}
person = {
    "name ":"pratap",
    "age":24,
    "work ":"devolepr ",
    "city ":"bengalore ",
   
}

person.clear()
print(person)


# set default
person = {
    "name ":"pratap",
    "age":24,
   
}
person.setdefault("age", 24)
print(person)

person.setdefault("name", "Bob")
print(person)


#  creat a dictioneris by keys 
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)


