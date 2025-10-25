# Selection Sort in Descending Order
size = int(input("Enter the size of an array: "))
arr = list(map(int, input("Enter the values of array (comma separated): ").split(',')))

for i in range(size):
    max_index = i
    for j in range(i+1, size):
        if arr[j] > arr[max_index]:
            max_index = j
    arr[i], arr[max_index] = arr[max_index], arr[i]

print("Sorted array:")
print(*arr, sep=", ")
# Insertion Sort in Descending Order
size = int(input("Enter the size of an array: "))
arr = list(map(int, input("Enter the values of array (comma separated): ").split(',')))

for i in range(1, size):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] < key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

print("Sorted array:")
print(*arr, sep=", ")
# Bubble Sort in Descending Order
size = int(input("Enter the size of an array: "))
arr = list(map(int, input("Enter the values of array (comma separated): ").split(',')))

for i in range(size - 1):
    for j in range(size - i - 1):
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array:")
print(*arr, sep=", ")
