import string
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

def menu(room_items, inv_items):
    # Display menu
    print_menu(room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input



def print_menu(area_items, inv_items):
    print("You can:")    
    # Print the exit name 
    print_exits()
    for i in area_items :
        print("TAKE " + i["id"].upper() + " to take " + i["name"] + ".")
    for i in inv_items :
        print("DROP " + i["id"].upper() + " to drop " + i["name"] + ".")
    if current_area == bar_area:
        print("TALK to the barman")
    if current_area == seating_area:
        print("TALK to mate")
    if current_area == table_area:
        print("TALK to the girl")


        
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
            execute_go(command[1])
            
        else:
            print("Go where?")
            input("------->PRESS ENTER TO CARRY ON<------")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")
            input("------->PRESS ENTER TO CARRY ON<------")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Take what?")
            input("------->PRESS ENTER TO CARRY ON<------")
    
    elif command[0] == "talk":
        if len(command) > 1:
            execute_talk(command[1])
        else:
            print("Talk to who?")

    elif command[0] == "buy" and current_area == bar_area:
        if len(command) > 1:
            execute_buy()
        else:
            print("Buy what?")
        


    
    else:
        print("This makes no sense.")
        input("------->PRESS ENTER TO CARRY ON<------")

def execute_buy():
    if item_wallet and item_id in inventory:
        print("BUYING drink SCRIPT")
        inventory = inventory + item_drink
    else:
        print("GETTING REFUSED SCRIPT")
        
    




    

def execute_talk(person):
    global inventory
    if person == "barman" and current_area == bar_area:
        print("PRINT BARMAN SCRIPT")
        input("------->PRESS ENTER TO CARRY ON<------")
        return
    if person == "girl"and current_area ==  table_area :
        print("PRINT GET GIRL NUMBERS SCRIPT")
        input("------->PRESS ENTER TO CARRY ON<------")
        return
    if person == "mate" and current_area == seating_area :
        print("PRINT TALK TO MATE SCRIPT")
        print("PRINT MATE ASKED FOR ID")
        if item_mates_id in inventory:
            input("------->PRESS ENTER TO GIVE HIM HIS ID<------")        
            inventory.append(item_wallet)
            inventory.append(item_id)
            
        input("------->PRESS ENTER TO CARRY ON<------")
        return
    
    else :
        print("talk to who.....?")
        input("------->PRESS ENTER TO CARRY ON<------")
    



def execute_go(new_area):
  
    
    global current_area

    if new_area == "booth" or "bar" or "table" or "toilet"  or "seating":
        current_area = rooms[new_area]
   
    else :
        print("GO where....?")
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
                
    if x == 0:
        print("You cannot take that.")
        input("------->PRESS ENTER TO CARRY ON<------")
    
    





current_area = booth_area
inventory = []




# This is the entry point of our program
def main():
    #intro goes here
    print("""Your eyes slowly open as you regain consciousness, still pissed and spinning.
You’re sat at a pink leather booth.
Around you are 4 mini-stages and 2 private rooms.
There’s an exotic dancer entertaining countless eyes on the main stage.
The bar tender stands tall, grinning and wiping down the last beer glass.
In-front of him are 7 stools, the very last filled by a man drinking Russian Vodka.
He seems familiar.""")
    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        print_map()
        print_room(current_area)        
        print_inventory_items(inventory)
        # Show the menu with possible actions and ask the player
        command = menu(current_area["items"], inventory)
        
        # Execute the player's command
        execute_command(command)

        
         
        
        print("##############################################################################################################")

main()