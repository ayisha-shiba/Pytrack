array questions:
#  Accept array input from user
size = int(input("Enter the size of Array 1: "))
arr1 = []

print("Enter the values of Array 1:")
for i in range(size):
    val = int(input())
    arr1.append(val)

# Copy the array
arr2 = arr1.copy()

# Add elements to copied array
arr2.append(60)
arr2.append(70)

# Display both arrays before swapping
print("\nBefore swapping:")
print("Array 1:", arr1)
print("Array 2:", arr2)

# Swap arrays
arr1, arr2 = arr2, arr1

# Display both arrays after swapping
print("\nAfter swapping:")
print("Array 1:", arr1)
print("Array 2:", arr2)
