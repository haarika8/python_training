from ast import Break
import random
num = random.randint(1,10)
for i in range(0,3):
    user = int(input("guess the lucky number "))
    if user == num:
       print("you guessed the right number and the number is",num)
       Break
if user !=num:
    print("you guessed the wrong number and the number is", num) 