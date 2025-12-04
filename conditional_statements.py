#Conditional Statements In Python
#What Are Conditions
#A Condition is simply a statement than can be either true or false.

a = 33
b = 200
if b > a:
    print("My Name Is Naitik") #This Line Will Be Print Because Condition Is True

#Let's Practice More

marks = 80
if marks >= 80:
    print("You Are The Topper In The Class");

#More
num = int(input("Enter A Number:"));
if num % 2 == 0:
    print("This Is An Even Number");
else:
    print("This Is An Odd Number");


#More
age = 17
if age >= 18:
    print("You Can Vote");
else:
    print("You Can't Vote");

#Practice Question
num1  = int(input("Enter Any Number :"));
if num1 > 0:
    print("This Is A Positive Number");
elif num1 == 0:
    print("This Is Zero");
else:
    print("This Is A Negative Number");
