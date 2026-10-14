#starting points
skater_style = 0
athlete_style = 0
streetwear_style = 0

#always use capitles to answer ABC questions
print("Today we will determine your clothing style. Ready?")
input()
answer1 = input("What brand do you prefer. A JNCO B Nike C Bape")
if answer1 == "A":
    skater_style += 1
elif answer1 == "B":
    athlete_style += 1
elif answer1 == "C":
    streetwear_style += 1

answer2 = input("Do you prefer A super baggy jeans B sweatpants C barrel jeans")
if answer2 == "A":
    skater_style += 1
elif answer2 == "B":
    athlete_style += 1
elif answer2 == "C":
    streetwear_style += 1

answer3 = input("Do you prefer A graphic tees B dryfit tees C layers")
if answer3 == "A":
    skater_style += 1
elif answer3 == "B":
    athlete_style += 1
elif answer3 == "C":
    streetwear_style += 1

answer4 = input("Do you prefer A skate shoes B running shoes C chunky shoes")
if answer4 == "A":
    skater_style += 1
elif answer4 == "B":
    athlete_style += 1
elif answer4 == "C":
    streetwear_style += 1

answer5 = input("Finally, do you prefer A beanies B no hat C caps and beanies")
if answer5 == "A":
    skater_style += 1
elif answer5 == "B":
    athlete_style += 1
elif answer5 == "C":
    streetwear_style += 1

answer6 = input("do you like A baggy clothes B tighter clothing C in between")

print(f"Your final scores are {skater_style} for skater style, {athlete_style} for athletic style, and {streetwear_style} for streetwear style")

if skater_style > athlete_style and skater_style > streetwear_style:
    print("You like skater clothing")
elif athlete_style > skater_style and athlete_style > streetwear_style:
    print("You like athletic clothing")
elif streetwear_style > skater_style and streetwear_style > athlete_style:
    print("You like streetwear")


if skater_style > athlete_style and skater_style > streetwear_style or streetwear_style > skater_style and streetwear_style > athlete_style:
    print("You like baggier clothing most likely")
elif athlete_style > skater_style and athlete_style > streetwear_style:
    print("you like comfortable clothing")

print("Thanks for playing!")