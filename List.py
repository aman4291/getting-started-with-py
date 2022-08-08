list1= ["aman","naman","annant","Cricket","football","badminton","Aman","aman"]
list1.append("names")
print(list1)

list1.remove("names")
print(list1)

list1.pop(4)
print(list1)

list2=list1.copy()
print(list2)

print(list1.count("aman"))


list1.extend(list2)
print(list1)

list1.sort()
print(list1)

list1.insert(4,"here")
print(list1)
