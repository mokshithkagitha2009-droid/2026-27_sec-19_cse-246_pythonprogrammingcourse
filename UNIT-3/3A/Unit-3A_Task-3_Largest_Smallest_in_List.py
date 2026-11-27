mylist = []

n = int(input("Enter number of elements: "))

for i in range(n):
    x = int(input("Enter element: "))
    mylist.append(x)

print("Largest element:", max(mylist))
print("Smallest element:", min(mylist))
