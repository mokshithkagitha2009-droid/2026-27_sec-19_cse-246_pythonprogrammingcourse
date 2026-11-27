mylist = [10, 20, 10, 30, 20, 40, 50]

newlist = []

for i in mylist:
    if i not in newlist:
        newlist.append(i)

print("Original List:", mylist)
print("List without duplicates:", newlist)
