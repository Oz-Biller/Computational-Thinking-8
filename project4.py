import random 

word_list = ["heart","loopy","audio","laugh","ocean","trial","goofy","black","probe","taker","maker","curse","poker","beach","clock","pluck","truck","goopy","xylyl","crwth","daddy","snipe","crank","blank","truth","zesty","musty","dusty","rusty","block","clank","brain","claim","boink","poise","noise","plain","shame","train","apple","grape","peach","mango","lemon","berry","melon","guava","olive","papal","cider","bread","toast","honey","sugar","spice","salty","sweet","cream","flour","plant","grass","seeds","roots","bloom","petal","shrub","crown","stone","river","ocean","cloud","storm","sunny","windy","night","dream","smile","laugh","dance","music","piano","viola","sword","spear","chair","table","shelf","couch","rugby","scrub","crazy","brail"]
hidden_word = random.choice(word_list)





for i in range(100):
    guess_word = input()
    output = ""
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    if guess_word[1] == hidden_word[1]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    if guess_word[2] == hidden_word[2]:
        output += "🟩"
    elif guess_word[2] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[3] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"




    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
        print(f"It took you {i+1} guesses")