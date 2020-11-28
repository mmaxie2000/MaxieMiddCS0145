import json

def main():
    # TODO: allow them to choose from multiple JSON files?
    with open('spooky_mansion.json') as fp:
        game = json.load(fp)
    print_instructions()
    print("You are about to play '{}'! Good luck!".format(game['__metadata__']['title']))
    print("")
    play(game)


def play(rooms):
    # Where are we? Look in __metadata__ for the room we should start in first.
    current_place = rooms['__metadata__']['start']
    # The things the player has collected.
    stuff = ['Cell Phone; no signal or battery...']
    items = []

    while True:
        print("")
        print("")
        # Figure out what room we're in -- current_place is a name.
        here = rooms[current_place]
        # Print the description.
        print(here["description"],["items"])

        # TODO: print any available items in the room...
        # e.g., There is a Mansion Key.

        # Is this a game-over?
        if here.get("ends_game", False):
            break

        # Allow the user to choose an exit:
        usable_exits = find_visable_exits(here)
        # Print out numbers for them to choose:
        for i, exit in enumerate(usable_exits):
            print("  {}. {}".format(i+1, exit['description']))

        # See what they typed:
        action = input("> ").lower().strip()

        print ("You typed: ", action)
        
        # If they type any variant of quit; exit the game.
        if action in ["quit", "escape", "exit", "q"]:
            print("You quit.")
            break

        if action == "meow":
            print("No, Doja Cat, you are a cow. Now get back to escaping.")
            continue
        
        if action== "help":
            print_instructions()
            continue
        
        if action == "stuff":
            print (stuff)
            continue
        
        if action== "room":
            print(items)
            continue
        
        if action== "take":
            stuff.append(items)
            print("You have added items to your collection of stuff.")
            print(stuff)
            continue
        
        if action== "search" or "find":
            print(find_visable_exits(here))
        else:
            continue
            
        # TODO: if they type "stuff", print any items they have (check the stuff list!)
        # TODO: if they type "take", grab any items in the room.
        # TODO: if they type "search", or "find", look through any exits in the room that might be hidden, and make them not hidden anymore!
        
        # Try to turn their action into an exit, by number.
        try:
            num = int(action) - 1
            selected = usable_exits[num]
            current_place = selected['destination']
            print("...")
        except:
            print("I don't understand '{}'...".format(action))
        
    print("")
    print("")
    print("=== GAME OVER ===")

def find_visable_exits(room):
    """
    Given a room, and the player's stuff, find a list of exits that they can use right now.
    
    RETURNS
     - a list of exits that are visible (not hidden)!
    """
    usable = []
    for exit in room['exits']:
        if exit.get("hidden", False):
            continue
        usable.append(exit)
    return usable

def print_stuff():
    if i in stuff:
        print(stuff)
    else:
        print('there is nothing here')
        
def print_instructions():
    print("=== Instructions ===")
    print(" - Type a number to select an exit.")
    print(" - Type 'stuff' to see what you're carrying.")
    print(" - Type 'room' to print the items availiable in the room.")
    print(" - Type 'take' to pick up an item.")
    print(" - Type 'quit' to exit the game.")
    print(" - Type 'search' to take a deeper look at a room.")
    print(" - Type 'help' to print the instructions again.")
    print(" - Type 'search' to find an exit.")
    print("=== Instructions ===")
    print("")

if __name__ == '__main__':
    main()
