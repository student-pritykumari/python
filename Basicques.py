#sum of two numbers
#taking numbers as inputs,a and b
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

sum=a+b
print("Sum of 2 nos:", sum)

#'/' is used for division in float
# (25/5)=0.5
print(a/b)

#'//' is also used for division in integer
# (a//b)=5
print(a//b)

#id of given numbers in python
a=5
b=9

print(id(a))
print(id(b))

#swap between two numbers
a = int(input("Enter 1st1 no.: "))
b = int(input("Enter 2nd no.: "))
a,b = b,a
print(a,b)

#Even/Odd
a = int(input("Enter 1st no.: "))
if a%2==0:
    print("Even")
else:
    print("Odd")

#Greatest number between two numbers
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
if a>b:
    m=a
else:
    m=b
print(m)











