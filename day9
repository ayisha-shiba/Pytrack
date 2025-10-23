# Program to check if a string is a palindrome without using reverse() or slicing

string = input("Enter a string: ")
length = len(string)
is_palindrome = True

for i in range(length // 2):
    if string[i] != string[length - i - 1]:
        is_palindrome = False
        break
        

if is_palindrome:
    print("Entered string is a palindrome")
else:
    print("Entered string is not a palindrome")
# Program to add two 2D arrays

size = int(input("Enter the size of arrays: "))

print("Enter the values of array 1:")
arr1 = []
for i in range(size):
    row = list(map(int, input().split()))
    arr1.append(row)

print("Enter the values of array 2:")
arr2 = []
for i in range(size):
    row = list(map(int, input().split()))
    arr2.append(row)

# Sum of two arrays
sum_arr = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(arr1[i][j] + arr2[i][j])
    sum_arr.append(row)

print("Sum of 2 arrays is:")
for row in sum_arr:
    print(*row)
    # Program to calculate the grade of a student using weighted average

print("Enter the marks scored by the student:")

written_test = float(input("Written test = "))
lab_exams = float(input("Lab exams = "))
assignments = float(input("Assignments = "))

grade = (written_test * 70 / 100) + (lab_exams * 20 / 100) + (assignments * 10 / 100)

print("Grade of the student is", grade)
