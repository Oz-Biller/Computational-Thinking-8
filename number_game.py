import random
hidden_number = random.randint(1,100)
#print(hidden_number)
answer1 = int(input("guess a number 1-100"))
for i in range(2):
    if answer1 == hidden_number:
        print("Correct!")
        quit()
    elif answer1 > hidden_number:
        print("lower")
    elif answer1 < hidden_number:
        print("higher")
    answer2 = int(input("guess again, chud"))
    if answer2 == hidden_number:
        print("Correct!")
        quit()
    elif answer2 > hidden_number:
        print("lower")
    elif answer2 < hidden_number:
        print("higher")
    answer3 = int(input("guess again buddy"))
    if answer3 == hidden_number:
        print("Correct!")
        quit()
    elif answer3 > hidden_number:
        print("lower")
    elif answer3 < hidden_number:
        print("higher")
    answer4 = int(input("guess again buddy"))
    if answer4 == hidden_number:
        print("Correct!")
        quit()
    elif answer4 > hidden_number:
        print("lower")
    elif answer4 < hidden_number:
        print("higher")
    answer5 = int(input("guess again buddy"))
    if answer5 == hidden_number:
        print("Correct!")
        quit()
if answer5 != int:
    print("You lost, no more chances")