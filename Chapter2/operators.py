#Expressions
a = 10
b = 5
c = a + b
print("The sum of a and b is:", c);

#Arithmetic Operators

x = 10
y = 59

print(x + y)
print(x - y)
print(x / y)
print(x * y)
print(x ** y)
print(x % y)

#Comparison Operators
print(x == y)
print(x <= y)
print(x >= y)

#Logical Operators
print(x < y and x == 10)
print(x > y or x == 10) 
print(not(x < y and x == 10))
print(not(x > y or x == 10))

#Assignment Operators
x += y  
print(x)
x -= y
print(x)
x *= y
print(x)
x /= y
print(x)
x %= y
print(x)
x **= y
print(x)
x //= y
print(x)
x = 10  # Reset x to original value for further operations
x &= y
print(x)    
x |= y
print(x)
x ^= y
print(x)
x >>= 2
print(x)
x <<= 2
print(x)

#Bitwise Operators
a = 10  # 1010 in binary
b = 4   # 0100 in binary    
print(a & b)  # AND
print(a | b)  # OR  
print(a ^ b)  # XOR
print(~a)     # NOT
print(a << 2) # Left Shift
print(a >> 2) # Right Shift 
#Membership Operators
str1 = "Hello, welcome to the world of Python"  
print('welcome' in str1)
print('Python' not in str1)
print('Java' in str1)   
print('world' not in str1)
#Identity Operators
x = 50
y = 50
print(x is y)   
print(x is not y)
y = 70
print(x is y)
print(x is not y)
y = x
print(x is y)
print(x is not y)
y = x + 0
print(x is y)
print(x is not y)
y = x * 1
print(x is y)
print(x is not y)
y = x - 0
print(x is y)
print(x is not y)
y = x / 1
print(x is y)
print(x is not y)
y = x // 1
print(x is y)
print(x is not y)
y = x ** 1
print(x is y)
print(x is not y)
y = x % 1
print(x is y)
print(x is not y)
y = x + 10 - 10
print(x is y)
print(x is not y)
y = (x * 2) // 2
print(x is y)
print(x is not y)
y = (x + 20) - 20

print(x is y)
print(x is not y)   
y = (x - 10) + 10
print(x is y)

