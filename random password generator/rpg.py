import random

print("This is a random password generator")
password = ""
length = int(input("Enter the length of the password: "))
for i in range(length):
    password += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+~`|}{[]\:;?><,./-=')
print("your password is: " + password)
