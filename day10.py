i=1

while i<=5:
     print('hello shiba', end=" ")
     
     j=1
     while j<=4:
        
        print('beautiful', end = " ") #so this is the concept of nested loops it runs after one hello shiba four times
        j=j+1 
        i=i+1 
        print()
    

for i in range(1,21,2):
    
    print(i)
for i in range(10):
    if i%5 !=0:
        print (i)
x=int(input("Enter no of candies u want?"))
i=1
av =5
while i<=x:
    
    if i>av:
        print("out of stock")
        break
    print ("candy")
    i+=1
print('bye')
for i in range (1,101):
    if i%3==0 and i%5==0:
        continue
    print(i)
print("bye")
for i in range (1,101):#so here we get the even no's by excluding the odd one
    if i%2!=0:
        pass
    else:
        print(i)
        