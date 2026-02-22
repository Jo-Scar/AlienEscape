# This Function is to display instructions for the game
def show_instructions():
    print("-----------------------------------------")
    print("Space Station Survival: Escape The Alien!")
    print("Collect 6 items to win, or get caught by The Alien.")
    print("Move commands:go North,go South,go East,go West")
    print("Add to Inventory: get 'item name'")
    print("-----------------------------------------")

# This Function is going to display the players current status
def show_status(current_room, inventory, rooms):
    print(f"Current Location: {current_room}")
    print(f"Inventory: {inventory}")

    # this looks at the dictionary and lists the directions available
    options = [f"{mov_dir} to {room}" for mov_dir, room in rooms[current_room].items() if mov_dir != 'item']
    print(f"You can move: {' | '.join(options)}")

    # Check for items (excluding the Alien)
    if 'item' in rooms[current_room] and rooms[current_room]['item'] != 'The Alien':
        # This checks if the label 'item' exists in the current room's dictionary
            print(f"You see the {rooms[current_room]['item']}")
    print("-----------------------------------------")

def main():
    # Dictionary linking rooms and items
    rooms = {
        'Main Atrium': {
            'West': 'Storage Locker',
            'North': 'Science Lab',
            'South': 'Engineering',
            'East': 'Comm Center'
        },
        'Storage Locker': {
            'East': 'Main Atrium',
            'item': 'Flashlight'
        },
        'Science Lab': {
            'South': 'Main Atrium',
            'East': 'Escape Pod Bay',
            'item': 'Hazmat Suit'
        },
        'Engineering': {
            'North': 'Main Atrium',
            'East': 'Life Support',
            'item': 'Fuel Cell'
        },
        'Life Support': {
            'West': 'Engineering',
            'item': 'Oxygen Tank'
        },
        'Comm Center': {
            'West': 'Main Atrium',
            'North': 'Cryo-Stasis',
            'item': 'Navigation Chip'
        },
        'Cryo-Stasis': {
            'South': 'Comm Center',
            'item': 'Keycard'
        },
        'Escape Pod Bay': {
            'West': 'Science Lab',
            'item': 'The Alien'
        },

    }

    # Starting point
    current_room = 'Main Atrium'
    inventory = []

    show_instructions()

    # Gameplay loop
    while True:
        # Check to make sure number of items are collected before encountering The Alien
        if current_room == 'Escape Pod Bay':
            if len(inventory) == 6:
                print("You collected all items and can now fix the escape pod! You Escaped The Alien! You Win!")
            else:
                print(f"The Alien caught you. You had {len(inventory)} items out of 6... Game Over!")
            # This break statement will end the game if the player does not have all 6 items before entering the Escape Pod Bay
            break

        # Show status
        show_status(current_room, inventory, rooms)

        # Get input
        user_input = input("Enter your move: ").title().split()

        # Input Validation
        if len(user_input) < 2:
            print("Invalid input! Try 'go [direction]' or 'get [item]'.")
            continue

        command = user_input[0] # account for 'go' or 'get' in the users input
        target = " ".join(user_input[1:]) # account for north or Flashlight in users input, or double words like Oxygen Tank

        # only valid directions
        valid_directions = ['North', 'South', 'East', 'West']

        # Movement logic (Go North)
        if command == 'Go':
            if target not in valid_directions:
                print(f"{target} is not a valid direction. Use North, South, East, or West.")            
            elif target in rooms[current_room]:
                current_room = rooms[current_room][target]
            else:
                print(f"You can't go {target} from here! You ran into a bulkhead wall, OUCH!!!")

        # item logic (Get Flashlight)
        elif command == 'Get':
            if 'item' in rooms[current_room] and rooms[current_room]['item'] == target:
                if target not in inventory:
                    inventory.append(target)
                    print(f"You picked up the {target}! And has been added to your inventory!")
                    # remove item from current room so you are not able to pick it up again
                    del rooms[current_room]['item']
            else:
                print(f"There is no {target} in {current_room}.")
        
        else:
            print("I don't understand that command. Try using 'get' ")

if __name__ == "__main__":
    main()