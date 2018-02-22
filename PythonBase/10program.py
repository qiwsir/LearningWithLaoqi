#coding:utf-8

class Cat:
    def speak(self):
        print("meow!")

class Dog:
    def speak(self):
        print("Woof")

class Bob:
    def bow(self):
        print("Thank you, thank you.")

    def speak(self):
        print("Hello, welcome to the neighborhood!")

    def drive(self):
        print("beep, beep!")

def command(pet):
    pet.speak()

pets = [Cat(), Dog(), Bob()]

for pet in pets:
    command(pet)