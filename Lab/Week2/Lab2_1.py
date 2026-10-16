# แก้ไขโค้ดนี้ให้ถูกต้อง

num = int(input("Enter a number: "))


if num < 0:
    text = f"{num} is negative"
elif num > 0:
    text = f"{num} is positive"
else:
    text = f"{num} is zero"
print(text)


if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")