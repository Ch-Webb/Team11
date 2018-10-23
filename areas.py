from items import *
from Characters import *
booth_area = {
    "name": "booth",
    "description":
    """You return back to the booth.
There are prints of your body left on the pink leather seats.
There appears to be things sticking out of the joints of the sofa. Loose change? A phone? What could it be.""",
    "items": [item_mates_id],
    "characters":[]
    
}
bar_area = {
    "name": "bar",
    "description":
    """You approach the bar. The barman looks straight at you, eye brows raised, waiting for you to rally and place another order.
There are bottles stacked behind him and countless phones, keys, wallets and condoms in a once-new box labelled ‘lost and found’.
On your right is your friend, Sam. He is completed pissed and is wearing a non-removable Halloween mask, given to him at birth.
On your left is the town drunk, he never leaves.""",
    "items": [item_drink],
    "characters":[character_bartender]
}
table_area = {
    "name": "table",

    "description":
    """You approach the table. A girl sits there in her fancy clothes.
Her friends have abandoned her and her mascara is running.
She stirs the olive in her empty cocktail glass.
Suddenly, she sees you and her eyes glare up with hope.
‘A unicorn?’ she thinks, or another guy looking for a fling, never to call her again.""",
    "items": [],
    "characters":[character_girl]
}
toilet_area = {
    "name": "toilet",
    "description":
    """You enter the male bathroom, watching your step.
The floor is filled with unspeakable things.
There are three cubicles and 5 urinals.
In the corner cages the remains of a now-empty condom disposer. """,
    "items": [item_keys],
    "characters": []
}
exit_area = {
    "name": "exit",

    "description":
    """You approach the green neon exit signs.
There is a tall, handsome Russian man there.
He seems aggressive. You try to leave.
“I already told you: Not without a wallet, keys and ID!”.
He throws you back into the booth, and you loose consciousness.""",

    "win_description":
    """
//////////////////////////////////////////////////////////////////////////////////////////////////////////////
CONGRATS!
YOU HAVE DEFEATED THE BOUNCER, YOUR PHONE HAS BEEN RETURNED TO YOU
YOU GRAB YOUR MATE AND GET IN TO THE CAB BUT JUST BEFORE YOU LEAVE A WOMAN SHOUTS OUT,
ITS THE WOMAN FROM THE TABLE WHO YOU GOT THE NUMBER FROM.........
"THANKS FOR DEFEATING THE BOUNCER HES WAS A TWAT" SHE SAYS TO YOU AND ASKED TO COME BACK TO YOURS
UNDERSTANDING WHATS GOING ON YOU MATE JUMPS OUT THE CAB AND SAYS HE WILL BE FINE HES NOT IN A STATE LIKE YOU,
WITH THIS YOU LEAVE AND DRIVE OFF INTO THE SUNSET.

    """,
    "items": [],
    "characters":[character_bouncer]
}

seating_area = {
    "name": "seating",
    "description":
    """description of area""",
    "items": [],
    "characters":[character_friend]
    }

rooms = {
    "booth": booth_area,
    "bar": bar_area,
    "table": table_area,
    "toilet": toilet_area,
    "exit": exit_area,
    "seating": seating_area,
}




