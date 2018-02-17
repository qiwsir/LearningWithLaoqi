#coding:utf-8

import random

number = random.randint(1, 100)
guess = 0

while True:   #guess <= 8:
    num_input = input("Input one integer(1-100):")
    guess += 1    #guess = guess + 1
    
    if int(num_input) < 0 or int(num_input) >= 100:
        print("整数必须大于0小于100")
    else:
        num = int(num_input)
        if number == num:
            print("GOOD. 你用{0}次猜中了".format(guess))
            break    #go out from this loop, break loop
        elif number > num:
            print("Your number is smaller.")
        elif number < num:
            print("Your number is bigger.")
        else:
            print("Sorry.")
