from MyList import MyList

# Initializing list with an array
list1 = MyList([1, 2, 3, 4, 5])


# 1. len()
print("The length of the list is", len(list1), end="\n\n")      # 5

# 2. list[index]
print("The value at index 2 is", list1[2], end="\n\n")          # 3

# 3. list[index] = value
list1[2] = 0
print("The new value at index 2 is", list1[2], end="\n\n")      # 0

# 4. del list[index]
del list1[2]
print("The new value at index 2 is", list1[2], end="\n\n")      # 4

# 5. for item in list
print("List:")
for item in list1:
    print(item, end=" ")

print("\n")

# 6. if val in list
val = 6
if val in list1:
    print("The value is included in the list")
else:
    print("The value is not included in the list")
