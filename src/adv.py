from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",[Item("tin cans","scrap used to make tools and weapons")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",[Item("wooden table", "scrap used to create tools and weapons")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("water", "used to hydrate")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("fruit","used for food")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[Item("silver ore","used for currency and smithing")]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
# available_loot = Room

# Write a loop that:

# Prints the current room name
while True:

    print(player.location)
    # print(Room.print_loot)
   
    command = input("> choose direction: n,s,e,w or q for quit->>> ").split(',')

    if command[0] == 'q':
       print('game over') 
       break
        

    elif command[0] == 'n' and hasattr(player.location, "n_to"):
        player.location = player.location.n_to
         

    elif command[0] == 's' and hasattr(player.location, "s_to"):
        player.location = player.location.s_to
        
    elif command[0] == 'e' and hasattr(player.location, "e_to"):
        player.location = player.location.e_to
        
    elif command[0] == 'w' and hasattr(player.location, "w_to"):
        player.location = player.location.w_to

    else:
        print("YOU CAN NOT GO IN THAT DIRECTION!!!!")
  
 # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.