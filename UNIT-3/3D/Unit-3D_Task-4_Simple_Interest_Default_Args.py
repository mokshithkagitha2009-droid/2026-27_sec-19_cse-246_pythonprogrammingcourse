def simple_interest(p, t, r=5):
    si = (p * t * r) / 100
    return si

p = float(input("Enter principal amount: "))
t = float(input("Enter time: "))

print("Simple Interest with default rate:",
      simple_interest(p, t))

rate = float(input("Enter interest rate: "))

print("Simple Interest with given rate:",
      simple_interest(p, t, rate))
