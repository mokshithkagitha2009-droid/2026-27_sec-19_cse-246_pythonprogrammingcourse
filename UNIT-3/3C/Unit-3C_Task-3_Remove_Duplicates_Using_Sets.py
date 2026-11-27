mylist = [10, 20, 10, 30, 20, 40, 50, 30]

print("Original List:", mylist)

# Convert list into set
newset = set(mylist)

# Convert set back into list
newlist = list(newset)

print("List after removing duplicates:", newlist)
