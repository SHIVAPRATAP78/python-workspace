#Sets are commonly used for:

#Removing duplicates

#Fast membership checking (O(1))

#Finding common elements between lists

#Solving graph/DFS/BFS problems

#Two-sum type problems

#Example (remove duplicates):

nums = [1, 2, 2, 3, 4, 4]
unique = list(set(nums))
print(unique) #[1,2,3,4]
#
s = {1,3,5,6,3,1, "pratap"}
print(s, type(s))
# add method 
s.add(243)
print(s,type(s))

# update method 
s = {1,3,6,8,7,}
s.update([2,4,5,9,])
print(s)

s1 = {1 , 2}
s2 = {3 , 4}
print(s2)
 
#romove method 
s = {1,3,4,5,76,54,"parth"}
s.remove(3)
print(s,type(s))

#clear() method 
s = {1,3,4,5,76,54,"parth"}
s.clear()
print(s,type(s))

# remove method 
s ={1,2,3}
s.remove(2)
print(s)

# dicard method when we give input that not in set its shows no error 
s={1,3,4,6,7}
s.discard(8)
print(s)

# 