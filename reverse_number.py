# Python program to reverse a number
n = int(input("please give a number:"))
print("before reverse your number is :", n)
reverse =0
while n!=0:
    reverse =reverse * 10 + n%10
    n=(n//10)
print("After reverse: " ,reverse)    