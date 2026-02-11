a =(1,23,44,56,78,78,90,54,"partha","batman",True)
print(a)

no=a.count(78) # its count how mmany 78 are in that 
print(no)

no= a.index(90) # its count from 0 index to 90 
print (no) 


# repeat tuple method 
my_tuple =(1,2,3)
repeated = my_tuple * 3
print(repeated)

#membership you can check if an item exists in a tuple using 'in' method 
my_tuple =(1,2,3)
print(3 in my_tuple)
print(5 in my_tuple)

#length : use len() function get a leangth of tuple 
my_tuple=(1,2,3,4)
print(len(my_tuple))

#min and max to check the smallest and largest elements in a tuple 
my_tuple=(1,2,3,4,5)
print(min(my_tuple))
print(max(my_tuple))

#slicing in tuple 
my_tuple=(1,2,3,4,5,6,7,)
sliced = my_tuple[1:4]
print(sliced)

#unpacking in tuple 
my_tuple=(1,2,3)
a,b,c = my_tuple
print(a,b,c)