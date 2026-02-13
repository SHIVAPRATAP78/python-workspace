# union and intersec methods 
s1 = {1,3,12,34,56}
s2 ={4,6,7,3,45}

print(s1.union(s2))
# intersection method 
s1 = {1,3,5,7,9}
s2 = {3,4,1,7,8}
print(s1.intersection(s2))


#differnce method its shows set with elements in set 1 but not in set 2 
s1 = {1 ,2 ,3 ,4,9} 
s2 = {1,5,6,7,3}
print(s1.difference(s2)) # its like minus operator same method 

s1 = {1 ,2 ,3 ,4,9} 
s2 = {1,5,6,7,3}
print(s2.difference(s1))


#compareisin method (important)
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b)) # True


a = {1, 2}
b = {1, 2, 3}
print(b.issuperset(a)) # true 
 
# returns true if no commen element 
a = {1, 2}
b = {1, 2, 3}
print(a.isdisjoint(b))