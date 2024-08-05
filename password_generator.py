import random

number=int(input("Enter the number of password you want to generate: "))
length=int(input("Enter the length of password you want to generate: "))
chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%^&*()!1234567890'

for i in range(number):
    password=''
    for j in range(length):
        password+=random.choice(chars)
    print(password)