import os
import random
from dotenv import load_dotenv
import google.generativeai as genai

# --- Setup Gemini ---
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

# --- Tools ---
def roll_dice(sides=6, roller_name="You"):
    result = random.randint(1, sides)
    print(f"{roller_name} rolled  {result} (1-{sides})")
    return result

def generate_event():
    events = [
        "You enter a dark cave.",
        "You find a treasure chest.",
        "A wild goblin blocks your path!",
        "A mysterious merchant offers you magical items.",
        "You discover a healing fountain in the forest.",
    ]
    event = random.choice(events)
    print(f"Event: {event}")
    return event

# --- Agents ---
def NarratorAgent():
    event = generate_event()
    response = model.generate_content(f"As a fantasy game narrator, describe this event in 1 sentences: {event}")
    print("NarratorAgent:\n", response.text)

    if "goblin" in event.lower():
        MonsterAgent()
    elif "chest" in event.lower() or "merchant" in event.lower():
        ItemAgent()
    else:
        print("The adventure continue...\n")

def MonsterAgent():
    print("MonsterAgent engaged...")
    player_roll = roll_dice(roller_name="You")
    monster_roll = roll_dice(roller_name="Monster")

    if player_roll >= monster_roll:
        print("You defeated the monster!")
    else:
        print("You were defeated by the monster!")
        exit()

def ItemAgent():
    print("ItemAgent offers a reward...")
    item_prompt = "Give the player a magical item from a fantasy world and describe its effect."
    response = model.generate_content(item_prompt)
    print("ItemAgent:\n", response.text)

# --- Game Loop ---
def run_game():
    print("Welcome to the Fantasy Adventure Game!")
    while True:
        input("Press Enter to continue your journey...")
        NarratorAgent()

# --- Start ---
if __name__ == "__main__":
    run_game()
