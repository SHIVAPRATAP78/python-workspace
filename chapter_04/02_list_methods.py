bag= ["books","laptop","notebook","9","12.5", True,"pratap" ]
print(bag)

bag.append("partha")  # it will add the element "partha" to the end of the list
print(bag )

bag= ["books","laptop","notebook","9","12.5", True,"pratap" ]
bag.append("batman") # it will add the element "batman" to the end of the list
print(bag)


# sorting the list
list1 = [8,4,3,77,99,45,23,1,33,56] 
list1.sort()# it will sort the list in ascending order
print(list1)

#reversing the list
list2=[50,40,30,70,2,43,1,9,56]
list2.reverse()
print(list2)

# sorting the list in descending order

list1 = [8,4,3,77,99,45,23,1,33,56] 
list1.sort()# it will sort the list in ascending order
print(list1) 
list1.sort(reverse=True) # it will sort the list in descending order
print(list1)


# inserting an element in the list
list3 =[9,7,6,4,12,1,34,56,78,90]
list3.insert(3,100) # it will insert the element 100 at index 3 in the list
print(list3)

list3.insert(0,200) # it will insert the element 200 at index 0 in the list
print(list3)

#pop method in list
list4 = [9,7,6,4,12,1,34,56,74,90,101,]
list4.pop() 
print(list4)# it will remove the last element of the list
list4.pop(2) # it will remove the element at index 2 in the list

print(list4) 

list4 = [9,7,6,4,12,1,34,56,74,90,101,]
list4.pop(1) # it will remove the element at index 1 in the list
print(list4)
#pop method also returns the value that is popped from the list
list4 = [9,7,6,4,12,1,34,56,74,90,101,]
print("Value popped:", list4.pop(1))
print(list4)

#remove method 
list5 = [9,6,4,12,1,34,56,74,90,101,]
list5.remove(34)
print(list5)

