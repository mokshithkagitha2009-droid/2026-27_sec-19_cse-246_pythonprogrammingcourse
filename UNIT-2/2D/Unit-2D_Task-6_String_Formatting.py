name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Using format()
print("My name is {} and my age is {}".format(name, age))

# Using f-string
print(f"My name is {name} and my age is {age}")

# Using % operator
print("My name is %s and my age is %d" % (name, age))
