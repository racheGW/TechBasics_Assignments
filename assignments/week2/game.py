#The Quizzical Labyrinth - A game in python by Rachel Weller
# Some parts of this game were created with the assistance of ChatGPT by OpenAI
import time

print("""
            (Welcome To The Labyrinth)
    ^     °  (Enter ONLY If you DARE)
   / \\ °
  /___\\
  (°~°)  *
  / * \\ |
 /(   )\\|
  || ||
  () ()
""")

print("\"Welcome to our little labyrinth, throughout your journey you will encounter many a strange thing.\"")
print("\"But don’t you worry we do a thorough sweep of the labyrinth at the end of they day. So should you get lost and lose all hope hunker down and wait for nightfall.\"")
print("\"Ah, I see you bought our little sack pack for your journey for the low price of 9,99$. Comes with one flashlight, an energy bar and a flask of boiling hot sewage. Should it come to it you can feed the energy bar to our complimentary gigantic earth worms.\"")
time.sleep(15) #15 second pause
print("\"How are we feeling?\"") #First question
print("")

time.sleep(5)#5 second pause
print("1: Amazing, I can’t wait to go in!")
print("2: Why would I need a flask of boiling hot sewage?")

time.sleep(10) #10 second pause
try:
    answer = int(input("How are we feeling?"))
    if answer ==1:
        print("\"Let’s get going then, I love your enthusiasm. I do hope you make it. Off you go now!\"")
    elif answer ==2:
        print("\"What’s the sewage for you ask? Well, we can’t give you all the answers, can we? Let’s get going! Off you go now, I hope to see you on the other side!\"")
    else:
        print("\"I see you're more the silent type... Well off you go then!\"")
except ValueError:
    print("Please enter a valid number!")


time.sleep(10)
print("""
       _________
      |  _____  |
      | |  |  | |
      | |__|__| |
      |      _| |
      |         |
      |         |
    _______________
""")
time.sleep(5)
print("You enter the labyrinth, as soon as you step over the threshold an unsettling quiet comes over you.  Slowly you take a few steps towards the first crossroad.")

print("")
print("You now have two options:1. Left or 2. Right?")
print("")
time.sleep(5)

while True:
    try:
        question = int(input("Will you go 1. Left or 2. Right?"))
        if question == 1:
            print("After turning left you see a patch of haze ahead of you, I seems to be slowly creeping towards you. Still, it doesn't seem threatening, more like it is trying to show you something…")
            #Path A begins

            print("As you stand in front of the patch of haze it seems to be calling to you, its glow pulling you in")
            print("What do you do?")
            print("")
            print("1. I make my way towards the patch of haze.")
            print("2. Let me think this through before I make a decision.")
            time.sleep(10)
            follow_haze = input("Choose 1 or 2:")
            #Path A go through haze
            time.sleep(5)
            if follow_haze == "1":
                print("The closer I get the more my teeth start to chatter and I feel myself shivering. Oh no, I’ve made a mistake haven’t I. Will I ever be warm again?")
                #Path A.1
                print("Quickly now, you can either stumble back towards the entrance and wait to be rescued, or try and find a way out of this, what do you do? ")
                print("1. I stumble back towards the entrance and await my rescuers shivering and cursing my foolish nature")
                exit()
                print("2. I will try and persevere!")

                time.sleep(15)

                try:
                    haze_choice = input("What do you do?")
                    if haze_choice == "1":
                        print("This journey has ended for you")
                        exit()
                    elif haze_choice == "2":
                        print("Huzzah! The boiling hot sewage, of course! I pull out my flask and fuelled by the hot steam I make my way through the patch of haze. ")
                    else:
                        print("You have hesitated for too long and the cold overwhelms you. Lets hope those giant worms dont find you...")
                        exit()
                except ValueError:
                    print("Please enter a valid number. Either 1 for left or 2 for Right.")
            elif follow_haze == "2":
                        print("As you take a moment to think you see that the hedged around the patch of haze have frozen solid, and is that a squirrel lying there, frozen solid?")
                        print("What can I do?")
                        print("Huzzah! The boiling hot sewage, of course! I pull out my flask and fuelled by the hot steam I make my way through the patch of haze.")
            else:
                print("You are trapped in the haze while you hesitated... lets hope those rescuers find you before the worms...")
                exit()

           #Path B
        elif question == 2:
            print("After turning right you see a hooded figure emerge from the shadows, as you turn to look behind you you see the way behind has turned into a dead end. You must go on! The hooded figure glides towards you, but before you can react it opens its mouth and starts to speak…")
            print("Hello there traveler, don’t you worry all you must do to cross my path and emerge victorious is to answer this simple question. What grows smaller the older it gets? ")
            time.sleep(20)
            hooded_figure = int(input("What grows smaller the older it gets?"))
            if hooded_figure == "candle":
                print("Very good, very adept you are. Off you go now.")
            else:
                print("Well, well, well... looks like you'll be needing that flashlight sooner than you thought.")
                print("Everything goes dark and the next thing you know you are being carried out of the labyrinth on a stretcher.")
                exit()
            time,sleep(10)

        else:
          print("You must choose. The entrance to the labyrinth is long gone, only left or right remains")
    except ValueError:
            print("Please enter a valid number. Either 1 for left or 2 for Right.")

    #Next path for both A and B
    print("As you continue on you walk towards a crossroads")
    print("Do you go straight ahead, left or right?")
    print("1. I choose the left path.")
    print("2. I choose the right path.")
    print("3. I go straight ahead")
    time.sleep(10)
    try:
        crossroads =int(input("Do you go straight ahead, left or right?"))
        if crossroads == "1":
            print("There is nothing here, oh no where did my exit go")
            exit()
        elif crossroads == "2":
            print("You walk along the path and come upon a small child. You briefly wonder if child labour laws apply in mystical labyrinths before getting on with it.")
            print("The child looks up at you and smiles, holding up five little bottles, gesturing for you to choose one. As everyone knows refusing would be considered incredibly rude so don’t you even think about it.")
            time.sleep(10)
            try:
                choose_bottle = int(input("Choose a bottle (1-5):"))
                if choose_bottle == 1:
                    print("Uhh is this Sprite™?")
                elif choose_bottle == 2:
                    print("Uhh is this a Coke Zero™?")
                elif choose_bottle == 3:
                    print("Uhh is this sparkling water?")
                elif choose_bottle == 4:
                    print("Uhh is this Fanta™")
                elif choose_bottle == 5:
                    print("Oh, this one is empty...")
                else:
                    print("I see someone is feeling rude today...")
                    print("Well, that is not how this game goes. Why is it going dark, you ask?")
                    print("The journey has ended for you.")
                    exit()
                print("The child giggles and lets you pass before running ahead and disappearing.")
            except ValueError:
                print("That wasn't a number! The child frowns at you.")
                print("The shadows close in.")
                print("The journey has ended for you")
                exit()

        elif crossroads == "3":
            print("There is nothing here, oh no where did my exit go?")
            exit()
        else:
            print("You must choose a path!")
    except ValueError:
            print("Please enter a valid number!")

    time.sleep(5)
    #Step 3:
    print("As you continue dusk starts to creep in and all of a sudden all you can see are numbers floating in front of you. ")
    time.sleep(10)
    print("A deep voice, ask you “What are the first four digits of pi?")
    time.sleep(10)
    first =input("What is the first digit")
    if first != "3":
        print("Someone has not been paying attention.")
        print("This journey has ended for you.")
        exit()

    second = input("What is the second digit")
    if second != "1":
        print("Someone has not been paying attention.")
        print("This journey has ended for you.")
        exit()

    third = input("What is the third digit?")
    if third != "4":
        print("Someone has not been paying attention.")
        print("This journey has ended for you.")
        exit()

    fourth = input("What is the fourth digit?")
    if fourth != "1":
        print("Someone has not been paying attention.")
        print("This journey has ended for you.")
        exit()

    print("Good job, you. The numbers slowly fade away and you make your way forward.")
    time.sleep(10)
    print("")
    print("As your legs start to feel heavy you look up and see a light ahead.")
    print("Eureka!")
    print("You’ve finally made it out of here.")
    print("")
    time.sleep(5)
    print("Unless what is that oh no a series of true or false questions are shooting at you.")
    print("(Yes, you read that right, ever heard of question bullets?)")
    print("(No, well now you have.)")
    print("")
    time.sleep(2)
    #check answers
    def ask_questions(questions, correct_answer):
        print(questions)
        answer = input("A or B").strip().upper()
        print("Lets take a look at that...")
        time.sleep(2)
        if answer != correct_answer.upper():
            print("That was wrong, bad luck, looks like you just missed the exit. Have fun in the dark. Your journey has ended here")
            exit()
        else:
            print("Very well, here is your next question...")
            time.sleep(1)
    #questions
    ask_questions("More people die from vending machines than from sharks. \nA. True \nB. False", "A")
    print("")
    ask_questions("The earth is round. \nA. True \nB. False", "A")
    print("")
    ask_questions("The moon landing was fake. \nA. True \nB. False", "B")
    print("")
    ask_questions("Alexander Hamilton was the first president of the United States of America. \nA. True \nB. False", "B")
    print("")
    ask_questions("The biggest animal in the world is the blue whale. \nA. True \nB. False", "A")
    print("")
    ask_questions("There are six world wonders. \nA. True \nB. False", "B")
    print("")
    time.sleep(5)
    print("\"Look at you smarty pants you’ve made it past the last challenge and have successfully found the exit\"")
    print("""
            (Welcome Back From The Labyrinth!)
    ^     °
   / \\ °
  /___\\
  (°~°)  *
  / * \\ |
 /(   )\\|
  || ||
  () ()
   """)
    time.sleep(5)
    print("\"Would you like to purchase some pictures we took during your bravest moments?\"")
    print("\"Only 29,99$?\"")
    time.sleep(3)
    print("\"No? Why didn’t I warn you about the labyrinth?\"")
    print("\"Well that would have ruined the surprise… Anyway have a great day, come again.\"")
