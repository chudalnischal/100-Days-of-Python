
# 📅 Day 5 – Password Generator 🔐

## 🔧 Project: Random Password Generator

On **Day 5** of my **100 Days of Python** journey, I built a **random password generator**! This tool allows users to create secure passwords based on how many **letters**, **symbols**, and **numbers** they want in it.

---

### 📚 What I Learned

- Using the `random` module to select characters randomly
- Creating and manipulating **lists** to build the password
- Using `input()` to take user-defined password criteria
- Using `random.shuffle()` to randomize the order of characters
- Joining a list into a string using `"".join()`
- Practicing **for-loops** and **range** to iterate through user-defined counts

---

### 🔍 Features

- Prompts user for:
  - Number of **letters**
  - Number of **symbols**
  - Number of **numbers**
- Calculates the total password length
- Randomly selects characters from predefined lists:
  - Letters (uppercase and lowercase)
  - Symbols (e.g., `!`, `@`, `#`, etc.)
  - Numbers (`0–9`)
- Shuffles all selected characters for better security
- Displays the final password to the user

---

### 🧾 Code

```python
import random

def main():
    print("Welcome to the Password Generator")
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
    letters_list = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers_list = list("0123456789")

    password_list = []
    for i in range(1, letters + 1):
        password_list.append(random.choice(letters_list))
    for i in range(1, symbols + 1):
        password_list.append(random.choice(symbols_list))
    for i in range(1, numbers + 1):
        password_list.append(random.choice(numbers_list))

    print("Shuffling password...")
    random.shuffle(password_list)
    password = "".join(password_list)
    print("Your Password is:", password) 
    print("Thank you for using the Password Generator")

if __name__ == "__main__":
    main()
```

---
### 🧠 Concepts Practiced

- String manipulation
- Loops and ranges
- Lists and randomization
- Taking and converting user input
- Building and combining multiple data types


📍 Check out my full 100 Days of Python journey in the main repository 