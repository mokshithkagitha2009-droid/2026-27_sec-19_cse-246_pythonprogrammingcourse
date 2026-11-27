mylist = []

n = int(input("Enter number of elements: "))

for i in range(n):
    x = int(input("Enter element: "))
    mylist.append(x)

print("List elements are:")

for i in mylist:
    print(i)
