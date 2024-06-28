#To search the element
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = (input("Enter the element : "))
    lst.append(ele)
search = input("Enter the element to search:")
if search in lst:
    print("Available")
else:
    print("Not Available")

#Swap first and second
ele=[10,20,"hello",5]
ele[0],ele[len(ele)-1] = ele[len(ele)-1],ele[0]
print(ele)

#Length
list=[1,2,3,4,"hello"]
print(len(list))


#To find minimum and maximum element
list=[1,3,5,2,4,6]
print(min(list))
print(max(list))

#Clear the list
list=[1,2,3,4,5]
list.clear()
del list

#Reverse
list=[1,2,3,4,5]
list.reverse()
print(list)

#Sum and Average
list=[1,2,3,4,5]
sum=0
for i in list:
    sum+=i
print(sum)
avg=sum/len(list)
print(avg)

#Count the occurence
list=[1,2,3,4,4,4,5]
print(list.count(4))

#Add and Delete
list=[1,2,3,4]
list.append(5)
list.pop(3)
print(list)