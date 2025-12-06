print("Naitik is learning Loops in Python\n");

#Loops Are Of Two Types
#1. For Loop
#2. While Loop

#Sabse Pehle While Loop
# print your name 100 times

num = 1
while num <= 5:
    print("Naitik")
    num += 1

#Let's Practice While Loop With Another Example
#Print numbers from 1 to 10

num1 = 1
while num1 <= 10:
    print(num1)
    num1 += 1

#Now Let's See For Loop
#Print numbers from 1 to 10 using For Loop

for i in range(1, 11):
    print(i)


#Print each character of a string using For Loop
my_string = "Naitik"
for char in my_string:
    print(char)

#Practice Questions

#Print all even numbers from 1 to 50
for even_num in range(2, 51, 2):
    print(even_num)


num2 = 10
while num2 >= 1:
    print(num2)
    num2 -= 1

#Print all odd numbers from 1 to 50

num = 1
while num <= 50:
    if num % 2 != 0:
        print(num)
    num += 1

#Print Sum Of First 10 Natural Numbers Backwise And Also take input from user

n = int(input("Enter a number: "))
sum = 0
while n >= 1:
    sum += n
    n -= 1
print("The sum is:", sum)
