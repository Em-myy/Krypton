
answers = "NIGERIA", "RICE", "MANGO"

print ("You have three chances.")
print ("Enter the correct answers for a country a food and a fruit to win the price.")
print ("A country that begin with 'n', a food with 'r' and a fruit with 'm' ")

guess_count = 0

while guess_count != 3:
    option_1 = str(input("Enter a country: "))
    option_2 = str(input("Enter a food: "))
    option_3 = str(input("Enter a fruit: "))
    
    selection = option_1.upper(), option_2.upper(), option_3.upper()

    score = 3 - (guess_count + 1)

    if selection == answers:
        print("You are correct.")
        break
    else:
        if score == 1 and 0:
            print("You are wrong.\nYou have " + str(score) + " attempt left")
        else:
            print("You are wrong.\nYou have " + str(score) + " attempts left")
    guess_count += 1
