import random


def main():
    print("Welcome to the Password Geenrator")
    print("How many letters would you like in your password?")
    letters = int(input("Enter number of letters: "))
    print("How many symbols would you like?")
    symbols = int(input("Enter number of symbols: "))   
    print("How many numbers would you like?")
    numbers = int(input("Enter number of numbers: "))
    total_password = letters + symbols + numbers
    print(f"Total password length is {total_password}")
    print("Generating password...")

    symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    letters_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    password_list = []
    for i in range(1, letters + 1):
        password_list.append(random.choice(letters_list))
    for i in range(1, symbols + 1):
        password_list.append(random.choice(symbols_list))
    for i in range(1, numbers + 1):
        password_list.append(random.choice(numbers_list))

    print("Shuffling password...")
    random.shuffle(password_list)
    password = ("".join(password_list))
    print("Your Password is:", password) 

    print("Thank you for using the Password Generator")


if __name__ == "__main__":
    main()
