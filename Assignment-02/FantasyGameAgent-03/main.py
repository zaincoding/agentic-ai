import random

# ---Tools --

def roll_dice(sides =6, roller_name="You"):
    result = random.randint(1,sides)
    print(f"{roller_name} rolled a {result} (1 -{result})")
    return result


def generate_event():
    events = [
        "You enter a dark cave",
        "You find a treasure chest",
        "A wild goblin block your path",
        "A mysterious merchant offer you items",
        "You discover a healing fountain"
        ]
    event = random.choice(events)

    print(f" Event {event}")

    return event

def narrator_agent():
    event = generate_event()
    if "goblin" in event:
        monster_agent()
    elif "treasure" in event or "merchant" in event:
        item_agent()
    else:
        print("The Adventure Continue...\n")

def monster_agent():
    print("\nMonsterAgent is engaged!")
    player_roll = roll_dice(roller_name='You')
    monster_roll = roll_dice(roller_name='Monster')

    if player_roll >= monster_roll:
        print("You defeated the monster!")
        item_agent()
    else:
        print("The monster overpowered you... Game Over!")
        exit()

def item_agent():
    print(f"\n ItemAgent activated... ")
    items = ["Golden Sword","Magic Ring","Healing Potion"]
    item = random.choice(items)
    print(f"you receive ***{item}***\n")
    print("Returning control to the narrator agent... \n")
    narrator_agent()

def start_agent():
    print("Welcom to the Fantasy Adventure Game.")


    while True:
        input("Press enter to continue the journey...")
        narrator_agent()

start_agent()
