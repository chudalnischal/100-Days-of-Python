import random

def main():
    print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    user_choice = int(input("Your choice: "))


    if user_choice >= 3 or user_choice < 0:
        print("Invalid choice. You lose.")
    else:
        ascii_art = [
            '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
            ''',
            '''
        _______
    ---'   ____)____
          ______)
          _______)
         _______)
    ---.__________)
            ''',
            '''
        _______
    ---'   ____)____
          ______)
           __________)
          (____)
    ---.__(___)
            '''
        ]
        computer_choice = random.randint(0, 2)
        print(f"Computer chose:\n{ascii_art[computer_choice]}")
        print(f"You chose:\n{ascii_art[user_choice]}")

        
        if user_choice == computer_choice:
            print("It's a draw.")
        elif (user_choice == 0 and computer_choice == 2) or \
             (user_choice == 1 and computer_choice == 0) or \
             (user_choice == 2 and computer_choice == 1):
            print("You win!")
        else:
            print("You lose.")



if __name__ == "__main__":
    main()