# intro
# user input : get the users name


start_of_game():
    # print map
    # print area title
    # print area descrption
    # print inventory
    # give the user options on what to do
    # execute users command

pickup() : # called when ever the user picks up an item
    # print "you picked up [item name]"
    # print item name
    # print item descipton
    # maybe offer a hint on how it could be helpfull to the users progress
    # place item in inventory
    # return back to the the room the user is in function with new item in inventory

give() : # this is called when ever the user needs to give a charictor something e.g. the girls phone number
    # print "you gave [item name] to the [charictor name]"
    # remove item from inventory
    # change a bool variable to true e.g. once the bartender has the number a varibale like bar_has_number = True
    # return back to the room the user is in function

    
inpected(): # called when the player wants to view an item
    # print item name
    # print item description
    # print item hint

    
booth_area():
    # print map
    # print area title
    # print area descrption
    # print inventory
    # give the user options on what to do[pick up and inspect id, inspect inventory , go to diffrent areas ]
    # execute users command


bar_area():
    # print map
    # print area title
    # print area descrption
    # print inventory
    # give the user options on what to do [talk to barman , talk to your mate , order drink(if you have id) ,inspect inventory, go to diffrent areas]
    # execute users command


talk_to_barman():
    # print charictor decription
    # print script
    # print users options[ go to table area and talk to girl, order a pint , go to other areas]
    # if the player gives the barman the number of the girl then he gets the script about the bouncer
    # options are printed again with the addition of the exit_area but can only go if they have wallet, id, house keys 
    # an option to go the toilet is also printed

table_area():
    # print map
    # print area title
    # print area descrption
    # print inventory
    # give the user options on what to do [talk to girl , inspect inventory , go to driffrent area]
    # if the player has her drink then he can also give the girl the drink and gets number in return wwhich goes in inventory
    # execute users command
    

talk_to_girl():
    # print charictor decription
    # print script
    # if player dosent have wallet or id then the game will hint to the user saying he needs to get these things
    # print player options[inspect inventory, if player failed at talking to the girl then he can try again like nothing happend, go to diffrent areas]


talk_to_mate():
    # print charictor decription
    # player can give id back if he does this then player gets wallet and his id back, the mates id is taken out of the inventory
    # print player options[go to diffrent areas, inspect inventory]

toilet_area():
    # print map
    # print area title
    # print area descrption
    # print inventory
    # give the user options on what they can do[go to diffrent area, inspect inventory, take a piss, explore booth 1,2 and 3 , pick up keys if player gets the right booth ]
    
exit_area():
    # print map
    # print area title
    # print area descrption
    # print inventory
    # fight bouncer script()
    # if the fight script returns false then player has to try fight again if it returns true the player has won
    # print player options[get mate and go home]
    
fight_bouncer_script():
    # fight the bouncer
    # work on how to win fight with group
    # return true or false

taxi_script():
    # print the deciption of the taxi and the inside
    # print the congrats and stuff







    
    
