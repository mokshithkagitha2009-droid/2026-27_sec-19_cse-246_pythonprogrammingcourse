a = {10, 20, 30, 40}

print("Original Set:", a)

# Membership testing
print("Is 20 present?", 20 in a)
print("Is 50 present?", 50 not in a)

# Add element
a.add(50)
print("After Add:", a)

# Remove element
a.remove(20)
print("After Remove:", a)

# Discard element
a.discard(100)
print("After Discard:", a)
