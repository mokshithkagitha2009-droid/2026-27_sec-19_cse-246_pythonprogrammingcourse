n = int(input("Enter a number: "))
total = 0

n = abs(n)

while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10

print("Sum of digits =", total)
