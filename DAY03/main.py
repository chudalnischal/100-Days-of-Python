# Treasure Island Game
# This is a simple text-based adventure game where the player has to make choices to find treasure.

def main():
    print(" Welcome to Treasure Island")
    print(" Your mission is to find the treasure.")
    print(" You are at a cross road. Where do you want to go?")
    print(" Type 'left' or 'right'")
    choice1 = input().lower()

    if choice1 != "left":
        print("You fell into a hole. Game Over.")
    else:
        print(" You come to a lake. There is an island in the middle of the lake.")
        print(" Type 'wait' to wait for a boat. Type 'swim' to swim across.")
        choice2 = input().lower()

        if choice2 != "wait":
            print("You get attacked by an angry trout. Game Over.")
        else:
            print(" You arrive at the island unharmed.")
            print(" There is a house with 3 doors. One red, one yellow and one blue.")
            print(" Which colour do you choose?")
            choice3 = input().lower()
            if choice3 == "red":
                print("Burned by fire. Game Over!" )
            elif choice3 == "blue":
                print("Eaten by beasts. Game Over!" )
            elif choice3 == "yellow":
                print(" You found the treasure! You Win!" ) 
            else:
                print(" Game Over!")
            

if __name__ == "__main__":
    main()