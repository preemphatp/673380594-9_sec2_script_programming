
# --- Pattern 1 ---
print("Pattern 1: Square")
size = 5
for row in range(size):
    for col in range(size):
        print("*", end="")
    print()

print()

# --- Pattern 2 ---
print("Pattern 2: Right-angled Triangle")
height = 5
for row in range(1, height + 1):
    for col in range(row):
        print("*", end="")
    print()

print()

# --- Pattern 3  ---
print("Pattern 3: Inverted Triangle")
for row in range(height, 0, -1):
    for col in range(row):
        print("*", end="")
    print()

print()

# --- Pattern 3b  Pyramid ---
print("Pattern 3b: Pyramid")
for row in range(1, height + 1):
    for space in range(height - row):
        print(" ", end="")
    for star in range(2 * row - 1):
        print("*", end="")
    print()