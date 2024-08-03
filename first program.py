 # string in variable
name1 = 'Prity'
name2 = "Kuamari"
name3 = '''khushi'''

print(name1)
print(name2)
print(name3)

# boolean in variable
age = 23
old = False
a = None
print(type(old))
print(type(a))

#  sum in python
a = 2
b = 5
sum = a + b
print(sum)

# ARITHMETIC OPERATORS 
a = 5
b = 3
print(a + b)
print(a - b)
print( a * b)
print(a / b)
print(a % b) #remainder
print(a ** b) #power(a^b)

# RELATIIONAL OPERATORS (=,!,<,>,<=,>=)
a = 40
b = 50

print(a == b)#False
print(a != b)#True
print(a >= b) #True
print(a > b) #True
print(a < b) #False
print(a <= b) #False

# ASSIGNMENT OPERATOR (=,+=,*=,%=,/=,**=)
num = 10
 #10+10 => 20
num += 10
print("num :",num)

# logical operators(AND, OR, NOT)
# NOT OPERATOR converts 'True' to 'False'
a = 20
b = 20
print (not True)
print(a < b)
# AND OPERATOR & OR OPERATOR
val1 = True
val2 = False

print ("AND operator", val1 and val2)

print ("OR operator",(a == b) or (a > b))

# Type conversion, automatically converts int to float
a = 2
b = 4.25

print (a + b) #2.0 + 2.45

# Type casting, manual conversion
a = float("2")
b = 4.25

print(type(a))

# input in python
name = input ("enter your name: ")
print ("welcome", name)

# result for input() is always str
int = "5"
val = float(input("enter some value: "))
print(type(val),val)


