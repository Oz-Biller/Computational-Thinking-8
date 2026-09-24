print("Hello, today you will make a few choices! Ready?")
input()
print("guidelines: if a choice is given, type in your answer as the choice was typed in. example: if the code gives you a choice to go to the mall, youre answer would be 'go to the mall' not 'mall'")
input()
print("Alright, let's go!")
answer1 = input("You finish school. Will you go home, or go to basketball practice?")
if answer1 == "go to basketball practice":
    answer2 = input("Will you listen to coach, or mess around?")
    if answer2 == "listen to coach":
        print("you play scrimmage, go home, eat, and sleep.")
    elif answer2 == "mess around":
        answer3 = input("Coach gives you the choice to run laps or do pushups")
        if answer3 == "run laps":
            print("you go home sore and tired, and go to bed")
        elif answer3 == "do pushups":
            print("you go home sore and tired, and go to bed")
elif answer1 == "go home":
    answer4 = input("Do you want to play games or watch tv")
    if answer4 == "play games":
        answer5 = input("you get hungry. do you go to daves hot chicken or chipotle?")
        if answer5 == "daves hot chicken":
            print("you are full and go home and sleep")
        elif answer5 == "chipotle":
            print("you are full and go home and sleep")
    elif answer4 == "watch tv":
        answer5 = input("you get hungry. do you go to daves hot chicken or chipotle?")
        if answer5 == "daves hot chicken":
            print("you are full and go home and sleep")
        elif answer5 == "chipotle":
            print("you are full and go home and sleep")