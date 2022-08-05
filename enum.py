mynames = ["annant", "vinay","aman","annant"]

# 1. Using For loop------

for index in range(0,len(mynames)):
        print(f'{index+1} -> {mynames[index]}')

# 2. Using for-each loop------ 

index=0
for ele in mynames:
    print(f'{index+1} -> {ele}')
    index+=1
# 3. Using enumerate---------

for index, name in enumerate(mynames):
    print(f'{index+1} -> {name}')

# 4. Using while loop---------

index=0
while(index<len(mynames)):
    print(f'{index+1} -> {mynames[index]}')
    index+=1


# output 
# 1 -> annant
# 2 -> vinay
# 3 -> aman
# 4 -> annant
    


