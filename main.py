class Player:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def getname(self, newname):
        self.name = newname

    def additem(self, item):
        self.items.append(item)

    def removeitem(self, item):
        self.items.remove(item)

    def printitems(self):
        for i in self.items:
            print(i)


time = 0
youth = False
boytalk = True
expect = False
police = False
location = ""
player = Player("", ["The Revolver's Calling Card", "Pocketwatch"])


def ending(expect, police, rope):
    # SPOILERS! SPOILERS! SPOILERS! SPOILERS!
    print("You part the curtain that leads to the presidential suite. The Duke is here. You recognize that white comb-over from his portrait in the city hall.\n"
          "He turns around, then looks you dead in the eye. A manic smile spreads over his face.\n"
          "\"Inspector " + player.name + "! I've been expecting you!\"\n"
          "He stands from his chair and extends a hand. At first, you believe it to be a handshake, until the silver glint in his hand says otherwise.\n"
          "A revolver. Pointed directly at your vital organs.")
    if not expect:
        print("You find yourself utterly baffled. What quarrel did the Duke have with you?")
    else:
        print("You stare him down, unable to be intimidated by a petty show of power. You'd expect that much from The Revolver.")

    print("\"I've been waiting a long time for this.\" His finger traces the trigger. \"The only one smart enough to stay on my tail. Barely, anyway.\"\n"
          "\"I'll take that as a compliment,\" you say. He only laughs.\n"
          "\"I'm gonna enjoy sending you to Hell, Inspector. Really. It's an honor.\"\n")

    if rope:
        print("His finger is getting dangerously close to that trigger. There must be something you can use as a makeshift weapon.\n"
              "Your mind goes to the rope you picked up backstage. It's not much, but it might save your life. You retrieve it and hold it in both hands.\n"
              "What will you do?\n"
              "1 - Loop it around the Duke's gun\n"
              "2 - Get behind the Duke and choke him")
        proceed = False
        while not proceed:
            choice = int(input())
            if choice == 1:
                proceed = True
                print("Thinking fast, you throw a coil of rope toward the Duke's hand. Before either of you can react, the gun's aim has already changed.\n"
                      "The Duke pulls the trigger, but the bullet's path has already been directed at the ground.")
            elif choice == 2:
                print("Immediately, you lunge forward to try and catch the Duke by the neck and subdue him.\n"
                      "BOOM.\n"
                      "The gun goes off. You feel a sharp pain in your ribs, followed by a serious shortness of breath. The bullet has punctured your lung.\n"
                      "\"It's been a good run, Inspector.\" The Duke walks away, and you are powerless to stop him. \"But I always win in the end.\"")
                exit()
            else:
                print("Unrecognized input. Try again.")
    elif not rope and expect:
        print("You're watching The Revolver's hand. The moment it makes a move, you duck. It's a good thing, too, because that slight hand movement turned into a gunshot.")
    elif not rope and not expect:
        print("At that, The Duke pulls the trigger. You, Inspector, were always a quick thinker. But you weren't quicker than a bullet.\n"
              "Even as you reach up to shield your body, it isn't enough. The bullet pierces your lung, and you're done for.\n"
              "\nThe last thing you hear is the maniacal cackling of the man that claimed your life.")
        exit()

    print("\nA collective gasp is heard throughout the theater as the gunshot makes itself known to everyone there. The Revolver curses.\n"
    "\"You're not slick, " + player.name + "!\"\n")

    if rope and expect:
        print("Before The Revolver can even finish that sentence, you advance and loop your coil of rope around his gun again. He can't even react before you've twisted it entirely out of his hand.\n"
              "\"I've got you, Revolver.\" While he wonders how you know his name, you dive for the gun. You manage to get a grip on it, and then bring yourself to your feet.\n"
              "\"You ain't got ANYONE!\" The Revolver lunges at you, but it's too late. You throw the gun over the balcony and get out of the way.\n"
              "The Revolver barrels into the railing, and you quickly maneuver over to his back. You know The Revolver, and you know that he's not the lightest on his feet.\n"
              "Quickly, you snag both his hands with the rope and tie them up. The Duke thrashes and curses and cries and wails.\n"
              "\"It's over,\" you say. \"I'll have you at the police station before the morning.\"\n"
              "All The Revolver can do is cry out in anger.\n"
              "\nYou have captured The Revolver. Great work, Inspector " + player.name + "!")
        exit()
    elif expect and police:
        print("\"Oh, but I am.\" You duck behind a chair. There's footsteps coming up the stairs. You can hear them.\n"
              "The Revolver laughs. \"Don't tell me you finally got the police to cooperate. I know you better than that.\"\n"
              "\"I'm afraid you don't know me at all, Revolver.\" You stay out of his line of sight. He should still have five bullets left.\n"
              "The Revolver fires another bullet, this one hitting the wall behind you. \"We'll see about that.\"\n"
              "Just then, a set of five or more police officers part the curtain of the presidential suite. The Revolver doesn't even have time to protest before he's disarmed and restrained.\n"
              "\"What? No, I'm not finished!\" He thrashes around, kicking and squirming like a captured animal.\n"
              "You back away toward the wall and catch your breath.\n"
              "\"Hands off me!\" The Revolver curses and yells and protests, but it's all in vain. Five against one is no contest, even if the 'one' in question is a serial murderer.\n"
              "There on the floor, your heartbeat slows. Your enemy is being detained. You'll keep your job.\n"
              "A smile begins to grow on your face.\n"
              "Finally. Inspector " + player.name + " gains the victory.")
        exit()
    elif rope and police:
        print("You stretch the rope between your hands. Combat training, don't fail you now.\n"
              "The Duke immediately fires another shot. This time, it's fortunate enough to miss.\n"
              "\"I can't believe my reputation's this bad,\" you quip, circling around the Duke. \"Being threatened by a Duke of all people...\"\n"
              "\"Come on, Inspector, don't you recognize me?\" He fires another shot, which misses.\"I'm The Revolver, " + player.name + ".\"\n"
              "\"Could have fooled me.\" You dive toward the Duke's feet, rope outstretched. It's not much, but it knocks him off balance.\n"
              "\"I thought The Revolver was smarter.\"\n"
              "Just then, a set of five or more police officers part the curtain of the presidential suite. The Revolver doesn't even have time to protest before he's disarmed and restrained.\n"
              "\"What? No, I'm not finished!\" He thrashes around, kicking and squirming like a captured animal.\n"
              "You back away toward the wall and catch your breath.\n"
              "\"Hands off me!\" The Revolver curses and yells and protests, but it's all in vain. Five against one is no contest, even if the 'one' in question is a serial murderer.\n"
              "There on the floor, your heartbeat slows. Your enemy is being detained. You'll keep your job.\n"
              "A smile begins to grow on your face.\n"
              "Finally. Inspector " + player.name + " gains the victory.")
        exit()
    elif (rope and not expect and not police) or (expect and not rope and not police):
        print("You smirk for a second, but that smirk fades soon after the Duke regains his bearings.\n"
              "\"You might be a fast thinker, Inspector,\" He fires. The bullet misses. \"But you're still alone.\"\n"
              "The truth of his words hits harder than the next bullet he fires. It hits your ribcage with a sharp pain.\n"
              "The Duke scoffs, lowering his gun. \"Some Inspector you are.\"\n"
              "Your vision fades as you sink to the ground.")
        exit()

print("\"As Violetta meets her end, so does the Duke. Be there, Inspector, or the consequences will be obvious.\"\n"
      "That is what the calling card said.\n"
      "Truly, are you sure you want to step into the shoes of that poor Inspector?\n"
      "Press 1 to proceed.")

choice = int(input())
if choice != 1:
    exit()

print("Your pocketwatch shows thirty minutes to the hour. You're making good time.\n"
      "Your shoes click on the pavement as you walk just outside the opera house. The air is biting in its chill, drawing the blood to your cheeks, but that matters little now. If you fail what you set out to do today, the cold will not be the only thing to draw out blood this night.\n"
      "\"Inspector! Inspector!\" You turn your head to see a bright-eyed young woman running your way. \"Is it true? Are you really going to catch him?\"\n"
      "Do you stop to talk to her?\n1 - Yes\n2 - No")

proceed = False
while not proceed:
    choice = int(input())
    if choice == 1:
        time += 1
        youth = True
        proceed = True
        print("\"If all goes well,\" you say, slipping your pocketwatch into your pocket. \"That all depends if I can find them before they find the Duke.\"\n"
              "\"You'll catch him, I just know it!\" The girl emphatically jumps, clearly thrilled to be speaking with you.\n"
              "\"Yes, well I'm quite good.\" You begin to turn away, but the girl lingers by your side. It's clear that she's rather enamored by you.\n"
              "You give her a sideways glance. \"Is that all?\" You ask.\n"
              "\"Oh, no! If it isn't any trouble, erm... would you sign this?\" She holds up a little diary or notebook of hers. \"Really, it's been my dream to meet you, and I want to help in any way that I can.\"\n"
              "Not a chance, you think to yourself. This is a job for professionals. Still, you sign her notebook. What you're not expecting, however, is the fountain that comes bursting from her mouth afterward.\n"
              "\"I truly do believe that the man you're looking for is a despicable character indeed. Don't you think so, Inspector? I surely do.\"\n"
              "You smile and nod as she keeps at this for longer than you'd like. It's important to be attentive to your fans. When you are a person who errs on the side of justice, fans are few and far between.\n"
              "Eventually, she departs. You tuned out much of her ramblings, but now the show is about to start. You'd better get your ticket fast.")
    elif choice == 2:
        youth = False
        proceed = True
        print("\"Pardon me, young miss, but I'm in a hurry.\" You keep walking, hoping that she doesn't nag at you for too long.\n"
              "\"Oh.\" She looks down, seeming dejected. \"S-sorry to bother you, Inspector. Good day.\"\n"
              "\"Yes. Good day.\" You forge on to the ticket booth. It's important to keep up appearances as an inspector. If someone took note of you wasting time on the job, it would come out of your reputation. Perhaps it's better this way.")
    else:
        print("Unrecognized input. Try again.")

print("\nThe ticket booth has a bit of a line, but luckily for you, you have a reservation. You slip into the reservation line smoothly.\n"
      "\"Surname?\" The woman in the ticket booth inquires.")

player.getname(input("What is your name? "))

print("\n\"Ah, Inspector " + player.name + ", we've been expecting you.\" She smiles and hands you your ticket. \"I trust you'll keep the Duke safe and sound.\"\n"
                                       "\"I had hoped it would be more confidential than that,\" you mutter, taking your ticket. \"Thank you.\"")

print("You depart quickly, to avoid wasting any more time. It is only when you have passed the doors of the opera house that you realize that the woman at the ticket booth had given you a small envelope along with your ticket.")
player.additem("Envelope")

proceed = False
while not proceed:
    print("\nThe main theater is ahead. What will you do?\n"
          "1 - Take a seat\n"
          "2 - Take a look around\n"
          "3 - Check your inventory")

    choice = int(input())
    if choice == 1:
        proceed = True
        print("You make your way to the seat. It's decent, and will allow you an ample view of the opera.\n"
              "As you sit down, you are confronted with the envelope the woman at the booth gave you. A telegram, most likely. You turn it over, and find that the return address is the police department.\n"
              "Open it?\n"
              "1 - Yes\n"
              "2 - No")
        proceed2 = False
        while not proceed2:
            choice = int(input())
            if choice == 1:
                proceed2 = True
                print("You settle down and open the telegram. It reads the following:\n"
                      "\"Inspector " + player.name + ", our regards to your investigation.\n"
                      "Be it known that we are considering your investigation as circumstantial in nature. Taking into consideration your history and faculties, we have little choice but to discredit your word in most cases and situations.\n"
                      "Please understand that any further breaches of the integrity of our Police Force will result in your termination.\"\n"
                      "\nDrat. All those missed marks are catching up to you. You quickly close the letter.")
            elif choice == 2:
                proceed2 = True
                print("You'd rather not hear from those blockheads at the Police Force any more than you have to. You pocket the telegram again.")
            else:
                print("Unrecognized input. Try again.")
        if time > 0:
            print("The opera is starting now. It would be rude to get up and leave just as the first act begins, so you settle in. La Traviata, after all, is your favorite opera.")
            location = "opera"
        else:
            print("The opera won't start for a few more minutes. Do you stay in your seat?\n"
                  "1 - Yes\n"
                  "2 - No")
            proceed2 = False
            while not proceed2:
                choice = int(input())
                if choice == 1:
                    proceed2 = True
                    print("You remain in your seat. La Traviata, after all, is your favorite opera.")
                    location = "opera"
                elif choice == 2:
                    proceed2 = True
                    print("An inspector's work is never done. You leave your seat before the orchestra starts tuning.")
                else:
                    print("Unrecognized input. Try again.")
    elif choice == 2:
        proceed = True
    elif choice == 3:
        player.printitems()
    else:
        print("Unrecognized input. Try again.")
# location hall
if not location == "opera":
    print("\nYou decide to wander the opera house. The building is truly vast, a veritable display of the wealth this city once saw.\n"
          "Which direction do you go?\n"
          "1 - The box seats\n"
          "2 - The toilet\n"
          "3 - Backstage")
    proceed = False
    while not proceed:
        choice = int(input())
        if choice == 1:
            proceed = True
            print("You suppose it's a matter of policy to visit the potential victim before their foretold demise. The Duke will be in his box seat, in the presidential suite.\n"
                  "You ascend the stairs and make your way up to the balcony. Directly ahead is the presidential suite, with its velvet curtains separating the rich from the rabble.\n"
                  "Do you enter?\n"
                  "1 - Yes\n"
                  "2 - No")
            proceed2 = False
            while not proceed2:
                choice = int(input())
                if choice == 1:
                    ending()
                elif choice == 2:
                    proceed2 = True
                    print("No, the poor man must be terrified out of his wits. Your presence would only remind him of the thread on his life.\n"
                          "You decide to return to the ground floor. Hopefully, you didn't miss much of La Traviata.")
                else:
                    print("Unrecognized input. Try again.")
        elif choice == 2:
            proceed = True
            boytalk = False
            print("You don't feel the particular need for the toilet at the moment, but you find yourself so restless that you have nowhere else to go.\n"
                  "As you approach the toilet, you see a gangly young man, no older than fifteen. The reason he catches your eye is less so his plain, dirty clothes and more the shifty stride of his walk.\n"
                  "And you know when someone's up to something when you see someone. Call it an inspector's instinct.\n"
                  "\"You there! Boy!\"\n"
                  "The boy freezes, his wide eyes staring at you.\n"
                  "\"Y-yes?\" He doesn't dare move as you approach him.\n"
                  "A distinctive scent hangs off his clothes. Gunpowder. You don't let your surprise show on your face.\n"
                  "What do you say?\n"
                  "1 - \"Come off it, boy, I'm not here to hurt you.\"\n"
                  "2 - \"You'd better tell me what you're up to, lad, or I'll give you something to be scared of!\"")
            proceed2 = False
            while not proceed2:
                choice = int(input())
                if choice == 1:
                    proceed2 = True
                    print("\"S-sorry.\" The boy calms down enough to move his limbs into a standing position.\n"
                          "\"Sorry for what? What's gotten you frightened?\" You lace your voice with gentleness. Honey catches more flies than vinegar.\n"
                          "\"I-I can't tell you. He'd have my head, he would...\"\n"
                          "\"Who is this 'he?'\"\n"
                          "\"The Duke. He'd have my head. Blow it clean off, he would.\"\n"
                          "You've never met the Duke, and yet that description seems odd. Blow his head off? Why?\n"
                          "\"D-don't look at me like that,\" the boy pleads. \"I know who you are. You're that Inspector. You were going to save the Duke.\"\n"
                          "\"Why, yes.\" Your expression turns quizzical. This boy doesn't have the makings of a murderer. But what he does have are the makings of an accomplice.\n"
                          "What do you say?\n"
                          "1 - \"I'll keep him safe. Don't worry.\"\n"
                          "2 - \"What did the Duke tell you to do?\"")
                    proceed3 = False
                    while not proceed3:
                        choice = int(input())
                        if choice == 1:
                            proceed3 = True
                            print("The boy gulps, a cast of sweat forming on his forehead.\n"
                                  "\"Thank you, Inspector " + player.name + ". Thank you. Can-... can I go now?\"\n"
                                  "You nearly laugh as you wave the boy away. \"Yes. Go your way, I'll handle it.\"\n"
                                  "With an awkward tip of his cap, the young man departs as quickly as his little legs can carry him.")
                        elif choice == 2:
                            proceed3 = True
                            expect = True
                            print("You can see his breaths getting quicker.\n"
                                  "\"You already know, don't you?\" He freezes up again. \"It's those detective skills. You already know.\"\n"
                                  "\"Maybe I do.\" You keep your calm, even through your bluff.\n"
                                  "\"P-promise I'm not in trouble! Please!\"\n"
                                  "\"I don't see what you have to worry about. Would you answer my question, then?\"\n"
                                  "He takes a deep breath. \"I-I'll tell you. As long as I won't get in trouble, I will.\"\n"
                                  "\"Go on.\"\n"
                                  "\"I... I was hired by the Duke. He gave me a five-dollar note to get him his gun.\"\n"
                                  "\"His gun? Well, I'd wager that's in self-defense.\"\n"
                                  "\"T-that's not all,\" the boy interjects. \"When I gave it to him, he did this awful-like laugh. Said that " + player.name + " was gonna get what was comin'.\"\n"
                                  "A chill runs down your spine.\n"
                                  "\"That's your name, Inspector. I dunno that he knew that I knew.\"\n"
                                  "\"What type of gun was it, boy?\"\n"
                                  "He seems a bit thrown. \"Ah, erm... A revolver, I think. Six chambers.\"\n"
                                  "... By Jove.\n"
                                  "You nod. \"I see. Thank you, boy, you've helped me greatly.\"\n"
                                  "\"R-really?\" His face brightens up. \"I really helped out the famous Inspector " + player.name + "?\"\n"
                                  "\"I daresay you were a great help.\" You ruffle the boy's hair, unable to resist his charm.\n"
                                  "\"Oh, thank you!\" His eyes sparkle as he smiles for the first time. \"Thank goodness I ran into you!\"\n"
                                  "He tips his hat, his legs seeming to carry him away against his will. You smile and nod.\n"
                                  "\"Be careful, now,\" you call out to him. \"There's dangerous men about.\"\n"
                                  "The boy has left the hallway.")
                        else:
                            print("Unrecognized input. Try again.")
                elif choice == 2:
                    proceed2 = True
                    print("The boy lets out what could be described as a squeak.\n"
                          "\"I didn't do it!\" His feet start moving, propelling him through the hall.\n"
                          "\"I didn't kill the Duke! I didn't!\"\n"
                          "You begin to pursue him, but he is much faster and much younger than you are. Before you can even round the corner, he's gone.\n"
                          "Drat. There goes an important lead.\n")
                else:
                    print("Unrecognized input. Try again.")
            print("\nYou return to your seat, making a mental note of what just happened. You'll unravel all this soon enough. It's only a matter of time.")
        elif choice == 3:
            proceed = True
            print("You slip into a secluded place backstage. The actors are getting ready to go onstage, only a few of them shooting you a glance as you walk in. It's a good thing you look like a theater bigwig right about now.\n"
                    "So far, no suspicious characters. Then again, The Revolver is famous for their disguises. Well, chiefly, they're famous for their murders, but their disguises take a close second place.\n"
                    "An unused length of rope sits on the floor. Will you:\n"
                    "1 - Attempt to speak with one of the actors\n"
                    "2 - Pick up the rope")
            proceed2 = False
            while not proceed2:
                choice = int(input())
                if choice == 1:
                    proceed2 = True
                    print("You do your best to flag down whoever crosses your path. However, everyone you attempt to communicate with doesn't seem interested in the slightest.\n"
                              "Actors.\n")
                elif choice == 2:
                    proceed2 = True
                    player.additem("Rope")
                    print("Someone could trip on this. Thank goodness you're here to clean up after everyone. Really, you could have been a governess instead of an inspector. You'd at least have fewer enemies.")
                else:
                    print("Unrecognized input. Try again.")

                print("\nThe sounds of the orchestra tuning weave all around the opera house. You take that as your cue to leave. If you linger any longer, the actors might trample all over you.")
        else:
            print("Unrecognized input. Try again.")

    print("You hurry back to your seat. Luckily for you, the first act has only just started. You can catch most of your favorite opera before the second act begins.")
else:
    # location opera
    print("\nThe lights darken and the overture comes into full swing. Before long, a collection of fine coats and gowns pours onto stage.\n"
          "It is Violetta's party to celebrate her wellness. You know the opera well.")

# passage of act 1 into act 2

print("On the stage, an actress in a pale gown sings back and forth with a man in a tailored suit. You may not know Italian, but you know the story just the same.\n"
      "The woman, Violetta, has not fully recovered from her illness, despite celebrating her recovery. The man is professing his love for her, but she waves him off.\n"
      "She loves someone else.\n"
      "\nThe first act passes by without incident. The actors and orchestra take a short break, and you gain new freedom to roam around the opera house.\n"
      "What do you do?")
proceed = False
while not proceed:
    print("\nThe main theater is ahead. What will you do?\n"
          "1 - Wait for the next act\n"
          "2 - Call the Police Department\n"
          "3 - Step outside\n"
          "4 - Check your inventory")

    choice = int(input())
    if choice == 1:
        proceed = True
        print("No need to rush. The investigation can wait. Besides, the calling card mentions that the murder will take place when Violetta dies. That would be the third act.")

    elif choice == 2:
        proceed = True
        print("You excuse yourself from your seat. It's time to make an important call. You're going to need backup sooner rather than later.\n"
              "The office is just by the entrance, and you make your way there with ease. You are the Inspector, after all, and the staff gladly show you to their telephone.\n"
              "You lean over to the telephone mounted on the wall, putting the speaker by your ear.\n"
              "What do you say?")
        if expect:
            print("1 - \"I need your forces immediately. The Revolver is in the building.\"\n"
                  "2 - Choose your own words.\n"
                  "3 - \"I've solved it. The Revolver isn't going to kill the Duke. He IS the Duke.\"")
        else:
            print("1 - \"I need your forces immediately. The Revolver is in the building.\"\n"
                  "2 - Choose your own words.\n")
        phone_call = ""
        proceed2 = False
        while not proceed2:
            choice = int(input())
            if choice == 1:
                proceed2 = True
                phone_call = "I need your forces immediately. The Revolver is in the building."
                print("\"Inspector,\" says the voice over the phone, \"I would've thought you'd received our telegram.\"\n"
                      "\"Yes. I did. But you have to listen-!\"\n"
                      "\"If we can't have a convincing argument, we're going to employ our forces where they're needed.\"\n"
                      "\"We need them HERE.\"\n"
                      "\"I don't hear a shred of evidence. Give me one, and we'll be on our way.\"\n"
                      "\"...\"\n"
                      "\"That's what I thought. Goodnight, Inspector.\"\n"
                      "They hang up.")
            elif choice == 2:
                proceed2 = True
                phone_call = str(input("Type your message here. "))
            elif choice == 3 and expect:
                proceed2 = True
                phone_call = "I've solved it. The Revolver isn't going to kill the Duke. He IS the Duke."
                print("\"Oh, really?\" The voice on the other end seems unimpressed. \"And you're sure about that?\"\n"
                      "\"Yes. I spoke to a boy. The Duke had paid him to retrieve his gun. He says the Duke swore revenge on me.\"\n"
                      "\"I hope this isn't one of your tall tales, " + player.name + ". If you waste police resources again, your career is over. Understood?\"\n"
                      "\"Yes. I'm absolutely sure.\"\n"
                      "\"... We'll be there before the show's over. Don't disappoint.\"\n"
                      "They hang up.")
            else:
                print("Unrecognized input. Try again.")

        txt = open("phonecall.txt", "w")
        txt.write(phone_call)
        txt.close()
        txt = open("phonecall.txt", "r")
        string = str(txt.read())
        txt.close()
        if "Duke" in string and "Revolver" in string:
            police = True
            print("\nIf you didn't know better, you'd say you actually won over the police department. It's a miracle, and a favor you won't forget.\n"
                  "... Even if it gets you fired.")
        else:
            print("\nNo matter how you look at it, that didn't go well. You take a deep breath and rub your eyes. Maybe this really is the last of Inspector " + player.name + ".")
    elif choice == 3:
        proceed = True
        print("It appears some fresh air is in order. While the opera is on pause, you slip out of the opera house.")
        if youth:
            print("In the corner of your eye, you see some activity. When you look at it, its form becomes clear. It's the girl you spoke to earlier. In other words, your biggest fan.\n"
                  "\"Oh! Hullo!\" The girl waves you down. \"I didn't think I'd see you again, Inspector!\"\n"
                  "\"Hello.\" You stop and speak to her, just as you did before. \"Isn't it a bit cold to be loitering about here?\"")
            if not boytalk:
                print("\"Oh, well...\" The girl looks a little bashful. \"I just hoped to see you again, Inspector.\"\n"
                      "Isn't that sweet. It feels nice to have someone rooting for you.\n"
                      "\"So? Have you caught him yet?\" She bounces on her toes.\n"
                      "You laugh. \"If I had, I might not be here right now. The Revolver's a crafty fellow, I'm sure you know.\"\n"
                      "Her expression warps with fear and delight at the mention of the Revolver. \"Oh, he IS.\"\n"
                      "\nThe two of you carry on chatting for some time, until the sounds of the overture come singing through the building. You bid her farewell and hurry back.")
            else:
                expect = True
                print("\"No, no, I simply HAD to see you, Inspector! It's about your case!\"\n"
                      "You raise an eyebrow. \"Oh? Do tell.\"\n"
                      "\"Well,\" she begins, preparing to launch into a tale, \"I was standing around here earlier, when suddenly, a boy nearly runs into me!\"\n"
                      "\"A boy?\"\n"
                      "\"Oh, ah... I suppose he was a young man. He was a bit older than me, see, but much too gangly to be a man. Anyways, he nearly runs into me, and I smell something on him!\"\n"
                      "\"His young-man-ly stench?\" You laugh.\n"
                      "\"Gracious, no!\" She smiles. \"Gunpowder! He smelled of gunpowder, and I just thought that was AWFULLY suspicious.\"\n"
                      "Now that catches your ear. \"Gunpowder? Whatever was he doing with gunpowder?\"\n"
                      "\"That's what I wanted to find out. So I asked him! He got terribly shaky and asked if he was in trouble, but I told him it was all right.\"\n"
                      "\"What did he say?\"\n"
                      "\"Well, first he asked me to keep a secret. I said yes. I always keep my secrets, you know.\"\n"
                      "\"Good girl.\"\n"
                      "She beams. \"Thank you! Anyway, he said he was paid by the Duke to get him his gun! And that's not all!\"\n"
                      "... Paid by the Duke? Maybe this girl has some valuable information after all. \"Well, what is it?\"\n"
                      "She's nearly bursting with excitement. \"He overheard the Duke swear revenge on YOU!\"\n"
                      "What? If what she says is true, what does that mean? \"Me, you say?\"\n"
                      "\"Yes! And I've got a theory I think you'll like, Inspector.\"\n"
                      "\"Well, out with it!\"\n"
                      "\"I think the Duke IS the Revolver.\"\n"
                      "... Now, that would be something. It would certainly slide a lot of pieces into place.\n"
                      "\"Well?\" She asks. \"Was I right?\"\n"
                      "\"I think...\" You raise your hand up to your chin. \"... I might need a new assistant after today.\" You wink.\n"
                      "The girl could very well burst from excitement. Her smile grows into a grin, and then an incredulous giggle. \"Really, Inspector?\"\n"
                      "\"We'll see.\" You hear the overture to the second act coming through the opera house. \"I have to catch him first.\"\n"
                      "She bounces in place. \"Yes! Thank you, Inspector! Now, go! You're going to miss the show!\"\n"
                      "You bid her a gracious smile and depart back into the building.")
        else:
            print("\nThe air is cold. It's not exactly pleasant, but it does soothe your nerves. Before long, the cold grows unbearable and you return to the warmth of the opera house.")
    elif choice == 4:
        player.printitems()
    else:
        print("Unrecognized input. Try again.")

# act 2

print("\nThe second act begins. The longest act by far, it takes the opera's most beloved characters from happiness to ruin in the span of a few songs.\n"
      "Through much of it, you find your mind much too occupied to really enjoy it. What a shame. You've always adored La Traviata.\n"
      "\nWhen the second act closes, you are well aware your time is at hand. The murder will happen in the next act, and you must be prepared.\n"
      "What do you do?\n"
      "1 - Go up to the box seats to see the Duke\n"
      "2 - Stay in your seat to watch the third act\n")

proceed = False
while not proceed:
    choice = int(input())
    if choice == 1:
        proceed = True
        ending(expect, police, "Rope" in player.items)
    elif choice == 2:
        proceed = True
        print("You cannot bring yourself to leave your seat.\n"
              "\nHalfway through the third act, a gunshot startles the crowd. You turn your eyes toward the presidential suite at the back of the theater, and see nothing but commotion.\n"
              "Someone has died tonight.")
    else:
        print("Unrecognized input. Try again.")
