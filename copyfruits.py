fruits =['apple','banana','cherry','citrus','mango','watermelon']
copyfruits=[]
e='e'
i=0
while i<len(fruits):
    if e in fruits[i]:
        copyfruits.append(fruits[i])
    i+=1    
print(copyfruits)