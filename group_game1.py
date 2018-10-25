import string
import random
from items import *
from areas import *
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'fat', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would' , 'area', 'got','hot','cuite']
def filter_words(words, skip_words):
#This function filters all unnecessary words using the list "skip words"
#and a list of words that has been split from the user input
    #Create new empty array
    important_words = []
    #Iterate through current list of words
    for i in words:
        #If the word isnt an "unnecessary word", add it to the important list
        if i not in skip_words:
            important_words.append(i)
    #output important list
    return important_words

def remove_spaces(text):
#This function removes all leading and trailing whitespace from the input
    #Create a flag to check if the string actually contains letters in the first place
    letterFound = False
    #iterate through each character in the text. If any one of them is a letter, proceed with the function
    for letter in text:
        if (letter.isalpha()) or (letter.isdigit()):
            letterFound = True
    if letterFound == True:
        #Create two pointers, like how a queue structure works
        left = 0
        right = -1
        #Trim each side of the string until a letter is found
        while text[left].isspace():
            left += 1
        while text[right].isspace():
            right -= 1
        right += 1
        #Return the portion of the string that hasnt been trimmed
        return text[left:right or None]
    else:
        #If the string doesnt actually contain any letters or digits, it will always
        #evaluate to "" so just return ""
        return ""
    
def remove_punct(text):
#This function removes all punctuation from an input string
    #Set up an empty string for the output to be stored in    
    no_punct = ""
    for char in text:
        #for each letter in the text, if its not in the predefined list of punctuation, add it to the output string
        if not (char in string.punctuation):
            no_punct = no_punct + char
    #Then return the output string
    return no_punct

def normalise_input(user_input):
#This function combines remove_punct and remove_spaces, and converts all input to lower case, normalising it.
    # Remove punctuation and convert to lower case
    no_punct = remove_punct(user_input).lower()
    #Remove leading and trailing whitespace
    no_spaces = remove_spaces(no_punct)
    #Split into list by the remaining spaces
    list_of_words = no_spaces.split()
    #Filter unnecessary words
    important_words = filter_words(list_of_words, skip_words)
    #Return this normalised input
    return important_words


def print_room(room):
#This function displays all information about the room the user is in
    # Display room name
    print()
    print(room['name'].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    # Display room items
    print_room_items(room)

def print_room_items(room):
#This function displays all the items that are in a room
    #Get the list of items from the dictionary room
    items = room["items"]
    #Split into list
    items = list_of_items(items)
    #If list is empty, return nothing
    if items == "":
        return
    #Else, return what is in the room
    print("There is " + items + " here.")
    print("")

def print_inventory_items(items):
#This user displays all the items that the user is holding
    #If you have no items, tell user you have no items
    if items == []:
        
        print("you have no items")
        print("")
    #Else, print the list of items that you do have
    else:
        print("You have" + list_of_items(items)+ ".")
        print("")

def list_of_items(items):
#This function splits a dictionary list into a normal, presentable string (ie all items separated with commas, etc)
    #Define empty output string
    list_of_things = ""
    x = 0
    #For all items in the list "items"
    for i in items:
        #Set i to the item name
        i = i["name"]
        x = x +1
        #if the pointer is at the end of the list, only add the item with nothing else
        if x == 1 :
            list_of_things = list_of_things + i
        #else, add the item, separated with a comma
        else:
            list_of_things = list_of_things + ", " + i
    #Return the string of items
    return list_of_things

def menu(room_items, inv_items, character):
#This function displays the menu for the user and takes an input, normalising it and passing it out
    # Display menu
    print_menu(room_items, inv_items,character)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)
    #Return normalised input
    return normalised_user_input

def print_menu(area_items, inv_items , characters):
#This function displays all of the actions that the user can perform
    print("You can:")    
    # Print the exit name 
    print_exits()
    #for each item in the area, display what can actually be done with it
    for i in area_items :
        if i == item_drink:
            print("BUY " + i["id"].upper() + " to take " + i["name"] + ".")
        else:
            print("TAKE " + i["id"].upper() + " to take " + i["name"] + ".")
    #Offer option of dropping user items
    for i in inv_items :
        print("DROP " + i["id"].upper() + " to drop " + i["name"] + ".")
    if current_area == bar_area:
        print("TALK to the barman")
    if current_area == seating_area:
        print("TALK to mate")
    if current_area == table_area:
        print("TALK to the girl")
    if current_area == exit_area:
        print("TALK to the bouncer")
    for i in characters:
        i = i["id"]
        print("LOOK AT " + i)
        
    print("What do you want to do?")
    
def print_exits():
#This function displays all of the available areas for the user to travel to
    #For all rooms, display each room
    #Bar is open plan, user can travel anywhere from anywhere
    for key in rooms:
            print("GO TO "+ key)

def execute_drop(item_id):
#This function allows the user to drop any given item in their inventory
    #Define flag to check if item is in inventory
    found = False
    #Search through inventory. If it's in there, remove from inventory and add to room's "inventory"
    #Update flag to show it's been found
    for element in inventory:
        if item_id == element["id"]:
            inventory.remove(element)
            current_area["items"].append(element)
            found = True
    #If item hasnt been found, it's not in the inventory and so cannot be dropped. Notify user.
    if found == False:
        print("You cannot drop that")

def execute_command(command):
#This function is the central hub for all commands. Any command the user makes is passed through here to a) check if it is valid and b) execute it
    if 0 == len(command):
        return
    #Modular design is repeated for each command. Decide what the command is, execute the command, and make sure the user has given an operand.
    if command[0] == "go":
        if len(command) > 1:
            try:
                execute_go(command[1])
            except:
                print("Go where?")
                input("------->PRESS ENTER TO CARRY ON<------")
            
        else:
            print("Go where?")
            input("------->PRESS ENTER TO CARRY ON<------")

    elif command[0] == "take":
        if len(command) > 1:
            try:
                execute_take(command[1])
            except:
                print("Take what?")
                input("------->PRESS ENTER TO CARRY ON<------")
        else:
            print("Take what?")
            input("------->PRESS ENTER TO CARRY ON<------")

    elif command[0] == "drop":
        if len(command) > 1:
            try:
                execute_drop(command[1])
            except:
                print("Drop what?")
                input("------->PRESS ENTER TO CARRY ON<------")
        else:
            print("Drop what?")
            input("------->PRESS ENTER TO CARRY ON<------")
    
    elif command[0] == "talk":
        if len(command) > 1:
            try:
                execute_talk(command[1])
            except:
                print("Talk to who?")
                input("------->PRESS ENTER TO CARRY ON<------")
        else:
            print("Talk to who?")
            input("------->PRESS ENTER TO CARRY ON<------")

    elif command[0] == "buy" and current_area == bar_area:
        if len(command) > 1:
            execute_buy()
        else:
            print("Buy what?")
            
    elif command[0] == "look":
        if len(command) > 1:            
            try:                
                execute_look(command[1])
            except:
                print("Look at who?")
                input("------->PRESS ENTER TO CARRY ON<------")
        else:
            print("Look at who?")
            input("------->PRESS ENTER TO CARRY ON<------")   
    else:
        print("This makes no sense.")
        input("------->PRESS ENTER TO CARRY ON<------")

def execute_look(character):
#This function allows the user to inspect each character, returning their name and description from the separate character file.
    a = characters[character]
    print("Their name is " + a["name"] + ", they are a " + a["description"])
    input("------->PRESS ENTER TO CARRY ON<------")

def execute_buy():
#This function allows the user to buy the drink from the barman
    global inventory
    global talked_to_girl
    #If the user is in possession of their wallet and id, and they have spoken to the girl, allow them to buy the drink from the barman
    if item_wallet and item_id in inventory:
        print("1")
        print(talked_to_girl)
        if talked_to_girl == True:
            print("2")
            print("""
You wander over to the bar and lean on it, the room spinning around you. The bartender wanders back over with an arm full of empty VKs and tips them into the bin.

He turns to you and raises an eyebrow.

“Well?”

“She wants a drink before she’ll give you her number mate.”

“smirnoff vodka, then. She’s been on them all night.”

“Alright, sounds good.”

He swiftly pours out a measure of Smirnoff and tops it up with Coke from the handheld tap behind the bar.

“This Smirnoff is nothing like real Russian vodka, like I used to have in Moscow. It’s like water in comparison.”

You nod, grabbing the drink as he sets it down on the bar.

“I’ll be back with her number in a minute,” you say, wandering away from the bar.
            """)
            input("------->PRESS ENTER TO CARRY ON<------")
            #In line with story, add drink to inventory
            inventory.append(item_drink)
        else:

            print("""
calling the bartender over

"one vodka please"

"got your wallet and id?"

"yes" you say annoyed as you pull them out to show him

he pours your drink and slides it too you

you pay and looking at makes you feel sick.....you down it in one


""")
            input("------->PRESS ENTER TO CARRY ON<------")
    elif not (item_wallet and item_id in inventory):
        #Refuse service to player who doesn't have wallet and id
        print("""'I TOLD YOU - NO MONEY, NO ID AND YOU'RE NOT GETTING A DRINK', the bartender says to you, looking rather annoyed""")
        input("------->PRESS ENTER TO CARRY ON<------")
        
def execute_talk(person):
#This function allows the user to speak to each different character.
    global inventory
    if person == "barman" and current_area == bar_area:
        if item_number in inventory:
            #If user has the number item, continue story
            print("""
You wander back to the bar yet again and lean on it, calling the bartender back over. He practically sprints back over, hope in his eyes.

“Well, did you get her number?”

You hold out your hand with the number scribbled on it. The bartender holds onto it for dear life, looking deeply into your eyes

“Um. No. Mate. The number’s on my hand.”

He blushes bright red and lets go as if he’s had an electric shock.

“Oh! Right. Sorry. Er… right. I’ll copy that down. What do you even do on a first date? Maybe we could listen to Tchaikovsky… no, no. Maybe just play Monopoly?”

He takes out his phone and keys in the number, saving it into his contacts, rambling on about Moscovian Monopoly and computer generated Tchaikovsky overtures. He then looks back up at you and nods towards the door.

“One of the bouncers picked up your phone. He’s outside now, a gentleman called Kirill. Average height, glasses, slight bit of a beard, dark hair. Russian bloke.”

“Like you, then?” You ask.

“Yeah, people say we look alike. I can’t see it myself.”

“Thanks.”

You turn from the bar and wander away. Time to get your phone off Kirill the Bouncer and go home, be sick into your toilet and pass out on the bedroom floor with your feet up the wall.
""")
            input("------->PRESS ENTER TO GIVE BARMAN THE GIRL'S NUMBER<------")
            #Remove the number from inventory
            inventory.remove(item_number)           
        else:         
            print("""You approach the bartender and look him up and down. You notice a small name tag on his black shirt that reads “K Sidorov.”

He wanders up and down the bar collecting empty VK bottles, then returns to you.

He peers over his glasses at you and scratches at his facial hair.

“We’re actually about to close,” he says, with a slight Russian accent.

“I need to find my phone, I lost it on the dance floor I think.”

“Oh, that was you. I see. Well…”

He looks at his watch, then peers back to you.

“Tell you what, you help me and I’ll help you?” he says, raising an eyebrow.

“Oh ho, a quid pro quo?”

“I suppose.”

He flicks his glance towards the table area, pointing towards a certain individual.

“See that girl at the table? I’ve been trying to get her number all night but I can’t get out from behind this damn bar. You get me her number, I’ll see if I can find out where your phone is. Fair?”

You sigh, slightly, then nod your head. You couldn’t help thinking that K Sidorov looked a bit like your mate.

Then again, people say that you and your mate look alike, but you’ve never seen it. Time to go get the bartender that girls number, you suppose. """)
            input("------->PRESS ENTER TO CARRY ON<------")
        return
    #If speaking to the girl
    elif person == "girl" and current_area ==  table_area :
        global talked_to_girl
        #Flag that user has spoken to character
        talked_to_girl = True
        #If user has the drink item, continue story
        if item_drink in inventory:
            print("""
You approach the girl on the dancefloor again and she turns to face you with a glint in her bespectacled eyes.

She asks in a vaguely Russian accent, “Is that for me?”

She eyes the vodka and coke hungrily. You nod, passing it over. She grabs it and skulls the whole thing, necking it in the way only a half-drunk fresher can.

“Alright, I did promise you my number, didn’t I?”

You take out a pen and scribble the number down on your hand as best you can, with the VKs and Jägerbombs coursing through your veins.

You nod your thanks and take your leave as the bearded girl continues to dance. Maybe now the bartender will tell you where your phone is.


""")
            input("------->PRESS ENTER TO GIVE GIRL DRINK<------")
            #Remove drink, give number
            inventory.remove(item_drink)
            inventory.append(item_number)
        else:
            talked_to_girl = True
            print("""You approach the girl the bartender pointed out and attempt to strike up a conversation. She eventually turns to you and peers at you through her glasses.

“Oh hello! Having a nice night?”

She asks, with an accent not unlike the bartender’s. Now you think about it, she’s got a beard a bit like the bartender’s as well. Whatever he’s into, you guess.

“Yeah, thanks! Look, the bloke at the bar wants your number but he can’t get round here to ask because he’s on shift. Any chance I could take it for him?”

She replies in her quietly accented voice, “Well, aren’t you sweet. Tell you what, if you can get me a drink, I’ll give you my number for that cute bartender. Thanks!”

And with that, she turned back towards the speakers near the tables and carried on dancing.

You roll your eyes and glance toward the bartender. You just want to go home and pass out already.""")
            input("------->PRESS ENTER TO CARRY ON<------")
        return
    #If speaking to friend, give user story hint
    elif person == "mate" and current_area == seating_area :
        print("""
You approach your friend on the dance floor, the pounding techno making your teeth rattle in your head.

He turns to face you, revealing dark hair drenched in sweat from the heat of the dance floor and slightly hazy eyes under his square glasses, probably from the VKs.

He shouts in slightly accented English over the blaring music.

“There you are! I have been looking everywhere for you!

"I'VE LOST MY ID" he says to you, "can you help me find it?"
""")
        input("------->PRESS ENTER TO CARRY ON<------")
        
        #If user has "mates id", continue story
        if item_mates_id in inventory:
            input("------->PRESS ENTER TO GIVE HIM HIS ID<------")
            print("As he reaches to put away his id he realises that he already has an id, your id, as well as your wallet.")
            print("""You look wrecked mate, you should probably get going home. You dropped your wallet and your keys earlier and then wandered off, so I grabbed them for you. Here you go!”

He hands over the keys and the wallet. Opening your wallet, you see your ID, confirming you are indeed over 18.

You thank him quietly, trying to remember what else you needed before you could leave the club.
""")
            inventory.append(item_wallet)
            inventory.append(item_id)
            inventory.remove(item_mates_id)
        input("------->PRESS ENTER TO CARRY ON<------")
        return

    elif person == "bouncer" and current_area == exit_area :
        print("""
You approach one of the bouncers, an average height, dark haired bloke. He turns to face you, revealing square glasses and a light dusting of hair on his chin.

He speaks softly, in a distinctly Russian accent. A name tag on his chest bears the name “Dr Kirill Sidorov.” What the hell is a bouncer doing with a doctorate?

“Can I help you, my friend?”

The man looks at you as if he’s had just about enough of his job, so you decide to make it quick.

“Hi, the bartender said you picked up my phone when I dropped it earlier?”

He narrows his eyes, his thin eyebrows furrowing.

“Are you accusing me of stealing your phone?”

Oh, god.

“No, no, not at all, I just thought that…”

He cuts you off, raising a hand.

“No, no. I was joking. I have your phone here.”

He rummages in his pocket, and as he does his name tags catches your eye again.

“So you’re a doctor?”

“Yes, I just work as a bouncer to pay for my collection of custom Monopoly sets and Tchaikovsky vinyls. I actually lecture Computer Science, you see.”

You can’t help but raise your eyebrows in surprise. He catches the incredulous look on your face and frowns.

The softly spoken Russian man advances towards you, stuffing your phone back into his jacket pocket.

“Is there something funny about Monopoly?”

In your drunken mind, there’s only one way this is going to end. A showdown with a softly spoken Russian bouncer with an affinity for Monopoly.

You hear the Pokémon combat music play in your head and raise your fists.
""")
        while fight() == False:
             fight()


def fight():
    input("------->PRESS ENTER TO CARRY ON<------")
    print("""You can:
    >PRESS 1 to Punch
    >PRESS 2 to Kick
    >PRESS 3 to RUN
""")
    rand = random.randint(1,3)
    print(rand)
    print("What will you do?")
    usermove = input(">")
    if usermove = rand:
        print("YOUR MOVE WORKS")
        input("------->PRESS ENTER TO CARRY ON<------")
        print("""
“You…you win…” he manages to mutter, fumbling your phone out of his pocket.

As you pick it up, the door of the bar bursts open as the loud, thunderous beat of the Russian National Anthem fills your ears.

Your chest fills with the pride of a nation, you have defeated one of its greatest representatives in the Western world.

The bartender, your friend, the bearded girl and everyone streams out to congratulate you, baptizing you in a stream of the purest Vodka you’ve ever tasted.

As the holy liquid covers you and pools around your feet, the crowd suddenly begins to chant ‘One of us...One of us...’

You look down, catching a glimpse of your reflection in the glistening liquid. Gone were your mediocre English features, replaced by the features of a small,

soft-spoken Russian face you’ve been seeing all night. You feel your knees weaken, your hands shaking as your lips part to mutter out the new name you’ve inherited.

“My name is…..Kirril…..Sidorov….
""")

        input("------->PRESS ENTER TO GO HOME<------")

        print("""
            //////////////////////////////////////////////////////////////////////////////////////////////////////////////
                        CONGRATS!
        YOUR PHONE HAS BEEN RETURNED TO YOU
""")
        input("PRESS ENTER TO SHUTDOWN THE GAME")
        quit()
               
    else:
        print("")
        print("THAT DID NOT WORK,TRY AGAIN")
        print("")
        return False



def execute_go(new_area):
#This function allows a user to move around the area
    global current_area
    #If the new area exists, move them there
    if new_area == "booth" or "bar" or "table" or "toilet"  or "seating" or "exit":
        current_area = rooms[new_area]
    else :
        print("Go where?")
        input("------->PRESS ENTER TO CARRY ON<------")
        
def execute_take(item_id):
#This function allows a user to pick up various items
    x = 0
    y= -1
    print("")
    for i in current_area["items"]:
        y = y + 1
        if item_id == i["id"]:
            x = 1          
            inventory.append(i)
            del current_area["items"][y]
            print("this is " + i["description"])
            input("------->PRESS ENTER TO CARRY ON<------")
    if x == 0:
        print("You cannot take that.")
        input("------->PRESS ENTER TO CARRY ON<------")

    
def print_map():
#This function prints a map of the area for the user to inspect.
    print("+---------------------+--+-------------------------------------------------------------------------------------------------------+--+--+--+--+--+")
    print("|    00      00       |  |        |BARMAN|                                                                              |-|      |  |  |  |  |  |")
    print("|   +---+   +---+     +--------------------------------------------------------------+                                  |-|      +--+--+--+--+--+")
    print("|00 |   |00 |   |00   +--------------------------------------------------------------+                                  |-|                     |")
    print("|00 |   |00 |   |00                               BAR   0000000000000000|MATE|000000                                    |-|                     |")
    print("|   +---+   +---+                                                       +----+                                          |-|                     |")
    print("|     00     00                                               SEATING AREA                                              +------+    +-----------+")
    print("|     00     00                                                                                                                                 |")
    print("|   +---+   +---+                                                                                                             TOILET            |")
    print("| 00|   |00 |   | 0+----+                                                                                                                       |")
    print("| 00|   |00 |   | 0|GIRL|                                                                                                                       |")
    print("|   +---+   +---+  +----+                                                                                                                       |")
    print("|     00      00                                                                                                                                |")
    print("|       TABLES                                                 BOOTHS                                                                           |")
    print("|               ****+--+--+ +------+ +--+--+ +------+ +--+--+ +------+ +--+--+ +------+ +--+--+ +------+ +--+--+****                            |")
    print("|               ****|  |  | |XXXXXX| |  |  | |XXXXXX| |  |  | |XXXXXX| |  |  | |XXXXXX| |  |  | |XXXXXX| |  |  |****                            |")
    print("|               ****|  |  | |XXXXXX| |  |  | |XXXXXX| |  |  | |XXXXXX| |  |  | |XXXXXX| |  |  | |XXXXXX| |  |  |****                            |")
    print("|               ****|  |  | |XXXXXX| |  |  | |XXXXXX| |  |  | |XXXXXX| |  |  | |XXXXXX| |  |  | |XXXXXX| |  |  |****                            |")
    print("|               ****+-----+ +------+ +-----+ +------+ +-----+ +------+ +-----+ +------+ +-----+ +------+ +-----+****                            |")
    print("+---------------------------------------------------------------------------------------------------------------------------    EXIT    +-------+")             
    print("                                                                                                                                        |BOUNCER|")
    print("                                                                                                                                        +-------+")
    



current_area = booth_area
inventory = []
talked_to_girl = False



# This is the entry point of our program
def main():
    print("""
INTRO.....

Your eyes slowly open as you regain consciousness, still pissed and spinning.
You’re sat at a pink leather booth.
Around you are 4 mini-stages and 2 private rooms.
There’s an exotic dancer entertaining countless eyes on the main stage.
The bar tender stands tall, grinning and wiping down the last beer glass.
In-front of him are 7 stools, the very last filled by a man drinking Russian Vodka.
He seems familiar.""")
    # Main gamee loop
    won = False
    while True:
        # Display game status (room description, inventory etc.)
        print_map()
        print_room(current_area)        
        print_inventory_items(inventory)
        # Show the menu with possible actions and ask the player
        command = menu(current_area["items"], inventory , current_area["characters"])        
        # Execute the player's command
        execute_command(command)
        print("######################################################################################################################################")

main()
