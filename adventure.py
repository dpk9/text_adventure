# text adventure
# David Kalish
import random

room_dict = {
    "room_one":
        {"monster": True},
    "room_two": {
        "monster": True,
        "key": True}
}

def main():
    health = 100
    have_key = False
    roomOne(health, have_key)

def roomOne(health, have_key):
    while True:
        print("You are in Room 1")
        if room_dict["room_one"]["monster"]:
            m_name = "skeleton"
            print("You have encountered a {}! Prepare for battle.".format(m_name))
            input()
            health = fight(health, m_name, 10)
            room_dict["room_one"]["monster"] = False
            print("Returning to Room 1")
        else:
            print("There's nothing here.")
        proceed = yesNo(input("Do you want to go to Room 2?\n"))
        if proceed:
            roomTwo(health, have_key)

def roomTwo(health, have_key):
    while True:
        print("You are in Room 2")
        if room_dict["room_two"]["monster"]:
            m_name = "zombie"
            print("You have encountered a {}! Prepare for battle.".format(m_name))
            input()
            health = fight(health, m_name, 15)
            room_dict["room_two"]["monster"] = False
            print("Returning to Room 2")
        if room_dict["room_two"]["key"]:
            take_key = yesNo(input("You see a key. Want to pick it up? y/n\n"))
            if take_key:
                print("You now have the key!")
                have_key = True
            else:
                print("You have left the key on the floor.")
        print("From here, you can go back to Room 1 or proceed to Room 3.")
        proceed = yesNo(input("Do you want to go to Room 3?"))
        if proceed:
            roomThree(health, have_key)
        else:
            proceed = yesNo(input("Do you want to go back to Room 1?"))
            if proceed:
                roomeOne(health, have_key)

def roomThree(health, have_key):
    gameOver()

def fight(p_health, m_name, m_health):
    while True:
        print("Attacking ", m_name)
        m_dam = random.randint(1, 10)
        m_health -= m_dam
        print("You did {} damage to {}. It has {} health remaining.".format(m_dam, m_name, m_health))
        input()
        if m_health <= 0:
            print("You killed the {}!".format(m_name))
            return p_health
        else:
            print("{} is attacking you!".format(m_name))
            p_dam = random.randint(1, 10)
            p_health -= p_dam
            print("{} did {} damage to you. You have {} health remaining.".format(m_name, p_dam, p_health))
            input()
            if p_health <= 0:
                gameOver()

def yesNo(y_n):
    while True:
        if y_n in ["y", "yes"]:
            return True
        elif y_n in ["n", "no"]:
            return False
        else:
            y_n = input("Invalid input. Use y/n.\n")

def gameOver():
    print("You have died. Game over.")
    retry = input("Try again? y/n\n")
    if yesNo(retry):
        main()
    else:
        exit()


if __name__ == "__main__":
    main()
else:
    print("Don't run the program like this")