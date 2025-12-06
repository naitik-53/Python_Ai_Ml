n = 1
while n <= 4:
    print("*" * n)
    n += 1
print("\n Your pattern is printed successfully!")

#Naitik Kumar Wants To Print His Name 5 Times , But each time with a number in front of it. Write A Program Using A While Loop That Prints:

i = 1
while i <= 5:
    print(f"{i} Naitik Kumar")
    i += 1
print("\n Name Printed Successfully!")

#Write A Program To Print The Multiplication Table Of Any Number Using A While Loop.

num = int(input("Enter A Number To Print Its Multiplication Table: "))

i = 1
while i <= 10:
    print(f"{num} * {i} = {num * i}")
    i += 1
print("\n Multiplication Table Printed Successfully!")