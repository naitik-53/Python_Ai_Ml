food_list = ["apple", "banana", "cherry", "date"]
for food in food_list:
    print(food)

for i in range(1, 6):
    print(f"{i} Naitik Kumar")

number = int(input("Enter a number to print its multiplication table: "))

for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
print("\n Multiplication Table Printed Successfully!")
n = 1   
while n <= 4:
    print("*" * n)
    n += 1
print("\n Your pattern is printed successfully!")

for list in range(2 , 20 , 2):
    print(list)

for i in range(2 , 20 , 2):
    print(i)


for m in range(2 , 20 , 2):
    if m == 10:
        break
    print(m)


#Print A Countdown Before Something "Exiciting" Happens Like "Laughing".
import time
count = int(input("Enter The Count Timer"))
print("/n CountDown Starts Now")

for i in range(count, 0 , -1):
    print(i)
    time.sleep(1)
print("\n Happy New Year")    

