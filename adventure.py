# text adventure
# David Kalish
import random

# Keep track of each room's contents
ROOM_DICT = {}

def main():
    """See bottom section for how this function gets called initially.
    The main() function starts the game.  It initializes the player's health,
    that they don't have the blue card, and resets the ROOM_DICT to its
    starting values. It then starts the first room.

    To add later: user chooses a difficulty, which raises or lowers their
    starting health.
    """
    health = 100
    have_blue_card = False
    global ROOM_DICT = {
        "room_one":
            {"monster": True},
        "room_two": {
            "monster": True,
            "blue_card": True}
    }
    roomOne(health, have_blue_card)

"""A dictionary is a data structure that has "keys" and "values." In the above
case, ROOM_DICT has two keys: room_one and room_two.  The values of those keys
are two new dictionaries; the room_one sub-dictionary has one key "monster"
with the value True.  The room_two sub-dictionary has two keys "monster" and
"blue_card", both values are True.

To access the a key's value, you do dict_name[key], which returns its value. So
to get room 2's key status, type
  > ROOM_DICT["room_two"]["blue_card"]
which will return
  > True

You can change a key's value too.
  > ROOM_DICT["room_two"]["blue_card"] = False
will change that blue_card value to False. You can mess things up if you're not
careful:
  > ROOM_DICT["room_two"] = False
will completely overwrite room_two's subdictionary containing monster and
blue_card with False, and you won't be able to access that information anymore.
"""

def roomOne(health, have_blue_card):
    """RoomOne has two arguments: health and have_blue_card.  Health is a
    number, which represents the player's health. have_blue_card tracks whether
    or not the player has the blue card.  These are statuses that persist
    throughout the game and need to be tracked through each room, whether
    they're used in that room or not.
    """
    global ROOM_DICT
    # always loop through the room in case the player doesn't proceed to the next room
    while True:
        print("You are in Room 1")
        # check to see if the room has a living monster.
        if ROOM_DICT["room_one"]["monster"]:
            # name the monster and give it health.
            m_name = "skeleton"
            m_health = 10
            print("You have encountered a {} with {} health! Prepare for battle.".format(m_name, m_health))
            input()
            # Go to the fight() function to battle the monster. It returns the
            # player's health, so be sure to save that data
            health = fight(health, m_name, m_health)
            # Update the room dictionary to track that you've already killed
            # the monster in this room, in case you come back here.
            ROOM_DICT["room_one"]["monster"] = False
        else:
            # You already killed the mosnter, and there's nothing else in this
            # room.
            print("There's nothing here.")
        # Ask player if they want to go to the next room. Use the yesNo()
        # function to validate their input.
        proceed = yesNo(input("Do you want to go to Room 2?\n"))
        # If the player wants to go to the next room, send them there.
        if proceed:
            roomTwo(health, have_blue_card)
        # Otherwise, let it loop back to the start of the room.

def roomTwo(health, have_blue_card):
    """The second room has a monster and a blue card.  Player fights the 
    monster if it hasn't been killed on a previous visit, and is prompted to 
    take the card if it hasn't been taken on a previous visit. The player can 
    either move on to Room 3 or return to Room 1.
    """
    global ROOM_DICT
    while True:
        print("You are in Room 2")
        if ROOM_DICT["room_two"]["monster"]:
            # this room has a zombie with 15 health
            m_name = "zombie"
            m_health = 15
            print("You have encountered a {} with {} health! Prepare for battle.".format(m_name, m_health))
            input()
            health = fight(health, m_name, m_health)
            ROOM_DICT["room_two"]["monster"] = False
        # if the blue card hasn't been taken already, ask the user if they want
        # to take it
        if ROOM_DICT["room_two"]["blue_card"]:
            take_blue_card = yesNo(input("You see a blue card. Want to pick it up? y/n\n"))
            if take_blue_card:
                print("You now have the blue card!")
                have_blue_card = True
            else:
                print("You have left the key on the floor.")
        print("From here, you can go back to Room 1 or proceed to Room 3.")
        # see where the player wants to go
        proceed = yesNo(input("Do you want to go to Room 3?"))
        if proceed:
            roomThree(health, have_blue_card)
        else:
            proceed = yesNo(input("Do you want to go back to Room 1?"))
            if proceed:
                roomeOne(health, have_blue_card)

def roomThree(health, have_blue_card):
    global ROOM_DICT
    gameOver()

def fight(p_health, m_name, m_health):
    """Handle monster fights. Three arguments. p_health is the player's health.
    m_name is the name of the monster. m_health is the monster's health.
    """
    # repeat the fight until the player or monster dies.
    while True:
        # attack monster first. get random damage to monster, subtract that
        # from the monster's health
        print("Attacking ", m_name)
        m_dam = random.randint(1, 10)
        m_health -= m_dam
        print("You did {} damage to {}. It has {} health remaining.".format(m_dam, m_name, m_health))
        input()
        # see if the monster is dead
        if m_health <= 0:
            print("You killed the {}!".format(m_name))
            # if the monster dies, end the fight and return the player's health
            return p_health
        else:
            # The monster attacks the player.  Random damage, subtract from
            # player's health.
            print("{} is attacking you!".format(m_name))
            p_dam = random.randint(1, 10)
            p_health -= p_dam
            print("{} did {} damage to you. You have {} health remaining.".format(m_name, p_dam, p_health))
            input()
            # If the player is dead, run the game over function.
            if p_health <= 0:
                gameOver()

def yesNo(y_n):
    """This function makes sure the user gives valid y/yes/n/no input. If they
    give invalid input, tell them so and let them re-enter their response.
    Don't exit this function until a valid response has been given (using a
    while True loop).
    """
    while True:
        if y_n in ["y", "yes"]:
            # an affirmative response returns True
            return True
        elif y_n in ["n", "no"]:
            # a negative response returns False
            return False
        else:
            # An invalid response, re-prompt the player.
            y_n = input("Invalid input. Try again with y/n.\n")

def gameOver():
    """Handles when the player dies.  It asks them if they want to try again or
    not.
    """
    print("You have died. Game over.")
    retry = input("Try again? y/n\n")
    # If they want to try again, go back to the main() function to reset
    # initial values and start over in the first room.
    if yesNo(retry):
        main()
    # If they don't want to try again, the program exits.
    else:
        exit()


"""This confusing, weird line is a special line for Python which checks for how
the program has been run.  The if-statement will return true if the program was
run from the terminal, i.e.

> python adventure.py

It will return false if this program is called from another program. This
situation shouldn't happen, so it prints a warning message and exits.
"""
if __name__ == "__main__":
    main()
else:
    print("Don't run the program like this")
    exit()