# --- Lab 3.1 Part 1: Single Number Multiplication Table ---
n = int(input("Enter a number for its multiplication table (e.g., 7): "))

for i in range(1, 13):
    print(f"{n} x {i} = {n * i}")

print()  

# --- Part 2: Full 12x12 Multiplication Grid (Challenge) ---
print("12x12 Multiplication Table:")
for i in range(1, 13):        
    for j in range(1, 13):    
        print(f"{i * j:4d}", end="")
    print()  