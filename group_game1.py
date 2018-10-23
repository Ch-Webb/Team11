import string
import random
from items import *
from areas import *
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would' , 'area', 'got','hot','cuite']
def filter_words(words, skip_words):
    important_words = []
    for i in words:
        if i not in skip_words:
            important_words.append(i)
    return important_words
def remove_spaces(text):
    letterFound = False
    for letter in text:
        if (letter.isalpha()) or (letter.isdigit()):
            letterFound = True
    if letterFound == True:
        left = 0
        right = -1
        while text[left].isspace():
            left += 1
        while text[right].isspace():
            right -= 1
        right += 1
        return text[left:right or None]
    else:
        return ""
def remove_punct(text):
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char
    return no_punct
def normalise_input(user_input):
    # Remove punctuation and convert to lower case
    no_punct = remove_punct(user_input).lower()
    no_spaces = remove_spaces(no_punct)
    list_of_words = no_spaces.split()
    important_words = filter_words(list_of_words, skip_words)
    return important_words

def print_map():
    # map image goes here
    print("map image")

def print_room(room):
    # Display room name
    print()
    print(room['name'].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    print_room_items(room)

def print_room_items(room):
    items = room["items"]
    items = list_of_items(items)
    if items == "":
        return
    print("There is " + items + " here.")
    print("")

def print_inventory_items(items):
    if items == []:
        
        print("you have no items")
        print("")
    else:
        print("You have" + list_of_items(items)+ ".")
        print("")

def list_of_items(items):
    list_of_things = ""
    x = 0
    for i in items:
        i = i["name"]
        x = x +1
        if x == 1 :
            list_of_things = list_of_things + i
        else:
            list_of_things = list_of_things + ", " + i
                    
    return list_of_things

def menu(room_items, inv_items, character):
    # Display menu
    print_menu(room_items, inv_items,character)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input

def print_menu(area_items, inv_items , characters):
    print("You can:")    
    # Print the exit name 
    print_exits()
    for i in area_items :
        if i == item_drink:
            print("BUY " + i["id"].upper() + " to take " + i["name"] + ".")
        else:
            print("TAKE " + i["id"].upper() + " to take " + i["name"] + ".")
    for i in inv_items :
        print("DROP " + i["id"].upper() + " to drop " + i["name"] + ".")
    if current_area == bar_area:
        print("TALK to the barman")
    if current_area == seating_area:
        print("TALK to mate")
    if current_area == table_area:
        print("TALK to the girl")
    for i in characters:
        i = i["id"]
        print("LOOK AT " + i)
        
    print("What do you want to do?")
    
def print_exits():
    for key in rooms:
            print("GO TO "+ key)

def execute_drop(item_id):
    found = False
    item = None
    for key in inventory:
        if item_id == key["id"]:
            item = key
        
    for element in inventory:
        if item_id == element["id"]:
            inventory.remove(element)
            current_area["items"].append(element)
            found = True
    if found == False:
        print("You cannot drop that")

def execute_command(command):
    if 0 == len(command):
        return

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
    a = characters[character]
    print("Their name is " + a["name"] + ", they are a " + a["description"])
    input("------->PRESS ENTER TO CARRY ON<------")

def execute_buy():
    global inventory
    if item_wallet and item_id in inventory:
        print("BUYING drink SCRIPT")
        input("------->PRESS ENTER TO CARRY ON<------")
        inventory.append(item_drink)
    else:
        print("GETTING REFUSED SCRIPT")
        input("------->PRESS ENTER TO CARRY ON<------")
        
def execute_talk(person):
    global inventory
    if person == "barman" and current_area == bar_area:
        if item_number in inventory: 
            print("GIVE BARMAN NUMBER SCRIPT")
            input("------->PRESS ENTER TO GIVE BARMAN THE GIRL'S NUMBER<------")
            inventory.remove(item_number)           
        else:         
            print("PRINT BARMAN SCRIPT")
            input("------->PRESS ENTER TO CARRY ON<------")
        return
    elif person == "girl" and current_area ==  table_area :
        if item_drink in inventory:
            print("print give girl drink")
            input("------->PRESS ENTER TO GIVE GIRL DRINK<------")
            inventory.remove(item_drink)
            inventory.append(item_number)
        else:            
            print("PRINT GET GIRL NUMBERS SCRIPT")
            input("------->PRESS ENTER TO CARRY ON<------")
        return
    elif person == "mate" and current_area == seating_area :
        print("PRINT TALK TO MATE SCRIPT")
        print("PRINT MATE ASKED FOR ID")
        if item_mates_id in inventory:
            input("------->PRESS ENTER TO GIVE HIM HIS ID<------")        
            inventory.append(item_wallet)
            inventory.append(item_id)
            inventory.remove(item_mates_id)
        input("------->PRESS ENTER TO CARRY ON<------")
        return
    else :
        print("Talk to who?")
        input("------->PRESS ENTER TO CARRY ON<------")

def execute_go(new_area):   
    global current_area
    if new_area == "booth" or "bar" or "table" or "toilet"  or "seating":
        current_area = rooms[new_area]
    elif new_area == "exit":
        fight()
    else :
        print("Go where?")
        input("------->PRESS ENTER TO CARRY ON<------")
        
def execute_take(item_id):         
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

def fight():
    global won
    rand = random.randint(1,3)
    while won == False:
        print("""You can:
    >Punch
    >Kick
    >Run
""")
        print("What will you do?")
        usermove = input()
        if normalise_input(usermove) == "punch":
            if rand == 1:
                print("won")
            else:
                return
        elif normalise_input(usermove) == "kick":
            if rand == 2:
                print("won")
            else:
                return
        elif normalise_input(usermove) == "run":
            if rand == 3:
                print("won")
            else:
                return
        else:
            print("I do not understand")
            input("------->PRESS ENTER TO CARRY ON<------")
        
        
    



current_area = booth_area
inventory = []




# This is the entry point of our program
def main():
    print("""Your eyes slowly open as you regain consciousness, still pissed and spinning.
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
        print("##############################################################################################################")

main()
