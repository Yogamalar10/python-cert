import random
answer=random.randint(1,10)
guess=[]
print("Welcome To Yoga's Math Game")
print("________________Have Fun!!________________")
print()
while True:
    print()
    print("Try guess the number i think:")
    number = int(input("Your guess (1-10):"))
    print()
    if number in guess:
        print("You aldready guess this number.")
        continue
    if number==answer:
        break
    else:
        print("Your answer is wrong.Try Again")
        guess.append(number)
        print("your old guess is :")
        for number in guess:
            print(number)
print("Congrats!!Your guess is right!")
print("_______________________________")
