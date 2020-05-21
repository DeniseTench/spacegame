import time

def capsule():
    print("Nothing in here, just some blood and guts. Ewwww!")
    time.sleep(2.0)
    room1_choices()

def cabinet():
    print("Some emergency procedures and a fire extinguisher. But no key codes.")
    time.sleep(2.0)
    room1_choices()

def bag():
    print("Some space food packets, Oxygen canisters and a weapon. A Laser Blaster 3000 gun. This might be useful.")
    time.sleep(2.0)
    room1_choices()

def chico():   
    print("Chico's collar has a four number sequence on it 7712. Meow.")
    room1_final_task()

def after_riddle():
    print("You press the intercom system button. You hear the same maniacal laughter and mutterings that you heard when you woke up. You recognise that voice. It's Captain Johnny Longjohns. 'I can see you there on the observation deck X ! Did you find my message? If you can solve all of my puzzles you might see me one last time before we're all dead! Otherwise just sit back and watch! MuHahahaha!'")
    time.sleep(0.5)
    print("'I always knew that guy was a madman. I must find him!' you think to yourself.")
    time.sleep(0.5)
    print("Please proceed to room 3")

def room_one():
    print("The Year is 2167. You are Lieutenant {} of the Starship Orion IV, a deep space military vessel.".format(name))
    time.sleep(4.0)
    print("You're on a scheduled return voyage to Earth after a routine 5-year patrol of the neighbouring star system Alpha Centauri.")
    time.sleep(4.0)
    print("Your last memory is settling down in your hypersleep capsule with the rest of your crew of 8 and Chico the cat.")
    time.sleep(4.0)
    print("Suddenly you awake from your deep slumber. Your capsule violently snaps open. Something is wrong!")
    time.sleep(4.0)
    print("Coming around from your abrupt awakening, you feel an intense pain in your head like you've been hit by a sledgehammer.")
    time.sleep(4.0)
    print("Your senses slowly start adjusting to the disastourous scene that now confronts you.")
    time.sleep(4.0)
    print("You hear the emergency sirens have initiated.")
    time.sleep(2.0)
    print("The dead bodies of your crew mates lie dormant in their opened hypersleep capsules, while others are empty.")
    time.sleep(4.0)
    print("The premature opening of a hypersleep capsule is, almost always, instantly fatal.")
    time.sleep(3.0)
    print("Something must have malfunctioned. You are lucky to be alive!")
    time.sleep(2.0)
    print("You look around the room. 5 crew members lie lifeless in their capsules. It looks like Chico the cat survived at least. Where are your other 3 ship mates, you wonder?")
    time.sleep(4.0)
    print("You suddenly notice that one of your crew mates is still alive and crawling towards the door.")
    time.sleep(4.0)
    print("It's Officer Gemma Hoskins. You stumble over to help her up, but as you reach her, it is obvious she is taking her last breaths.")
    time.sleep(3.0)
    print("You quickly try to open the door to the medical room by entering the usual code '0102' in the keypad. It responds with 'Access Denied'. The code has been changed!")
    time.sleep(5.0)
    print("Over the sound of the blaring emergency sirens, you can hear what sounds like the crazed cackling of someone over the ship's intercom system.")
    time.sleep(3.0)
    print("What the hell!!??")
    time.sleep(1.0)
    print("You go back to Officer Hoskins, turn her over on to her back, and as she coughs up blood all over you, she mutters 'The override code... check the ca......' You shake her but she's gone.")
    time.sleep(5.0)
    print("Looking around the room, you see a capsule, a cabinet, a cargo bag and Chico the cat.")
    room1_choices()

def room1_choices():
    response = input("Which do you check? [CAPSULE/CABINET/BAG/CHICO] ")
    if response == "CAPSULE":
        capsule()
    elif response == "CABINET":
       cabinet()
    elif response == "BAG":
        bag()
    elif response == "CHICO":
        chico()
    else:
        print("Sorry, I didn't understand the response. Please choose again from the four options.")
        room1_choices()

def room1_final_task():
    response2 = int(input("What is the code?"))
    if response2 == 7712:
        print("Well done! The door opens and you enter room 2.")
        room_two()
    else:
        print("Incorrect code. Try again.") #To make things more interesting, we could code in a three-strikes rule.
        room1_final_task()

def room_two():
    print("You find yourself on the ship's observation deck. Outside you can see that you've have arrived back to your home solar system.")
    time.sleep(2)
    print("The ship is travelling at high speed, passing close by the planet Jupiter. You are close to home, maybe less than 24 hours away.") 
    time.sleep(3)
    print("In the room you see some comfy chairs, a drinks dispenser, some potted plants and the intercom system on the wall. There is also something etched into one of the windows by a laser.")
    time.sleep(3)
    print("It reads: 'The more of this there is, the less you see. What is it?'")
    room2_riddle()

def room2_riddle():
    riddle1 = input("Answer the riddle: ")
    if riddle1 == "darkness" or "Darkness":
        print("Wow, that was a good guess.")
        room_three()
    else:
        print("Incorrect. Try again.")
        room_three

def room_three():
    print("A door opens and you walk through it into room 3.")

def start_game():
    global name
    name = input("Welcome to the space game. What is your name? ")
    time.sleep(1)
    print("Hello {}, great to meet you.".format(name)) 
    time.sleep(1)
    response = input("Are you ready to play? [Y/N] ")
    if response == "Y":
        print("Great, let's go.")
        room_one()
    elif response == "N":
        print("Fine then, be that way.")
    else:
        print("Try again, I didn't recognise that.")
        start_game()
start_game()
