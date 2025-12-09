#1.
user_name = input("Enter Your Name : ")
user_age = int(input("Enter Your Age : "))
user_city = input("Enter Your City : ")
print(f"Hey {user_name}, You Are {user_age} Years Old And You Live In {user_city}")

#2.
num1 = int(input("Enter The First Number : "))
num2 = int(input("Enter The Second Number : "))
print(num1 + num2)
print(num1-num2)
print(num1*num2)

#3.
input_string = input("Enter A String : ")
print(len(input_string))
print(input_string[0])
print(input_string[-1])

#4.
give_int = int(input("Enter An Integer Value"))
if give_int % 2 == 0:
    print("It Is An Even Number")
else:
    print("It Is An Odd Number")

#5.
numbers = [1,2,3,4,5]
print(max(numbers))

#6.
stringji = input("Enter A String : ")
vowels = "AEIOUaeiou"
if stringji == vowels:
    print(len(vowels in (stringji)))
else:
    print("There Is No Vowel")

    
#Ye humne aik function bnaya ha
def square ():
    square_num = int(input("Enter A Number Jiska Square Krna ha"))
    print(square_num ** 2)

#Calling The Function
square()