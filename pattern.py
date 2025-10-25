# for i in range(4):
#     for j in range (4-i):
#         print('#',end=" ")
#     print() 
    
nums =[12,23,2,48,4]
for num in nums :
    if num%5==0:
        print(num)
        break

else:
    print('not found')
num = 9


for i in range(2, num):
    if num % i == 0:
        print("Not prime")
        break
else:
    print("Prime")
def add(x,y):
    c=x+y
    print(c)
add(5,4)
name =input("Enter ur name: ")
age=input("Enter ur age: ")
print ("ur name is",name)
print("ur age is", age)