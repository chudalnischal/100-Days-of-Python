# 📅 Day 3 – Treasure Island Adventure Game 🏝️

## 🎮 Project: Treasure Island – A Text-Based Adventure Game

On **Day 3**, I built a fun **text-based adventure game** called **Treasure Island**. In this game, the player makes a series of decisions with the goal of finding the hidden treasure. Each choice affects the outcome — you either win or face "Game Over"!

---

### 🧠 What I Learned

- **Conditional statements** using `if`, `elif`, and `else`
- How to use **string methods** like `.lower()` to handle user input more effectively
- Using **nested conditionals** to create interactive stories
- Designing simple **game logic and flow**
- Taking and responding to **user input** using `input()`
- Writing clean and readable code using **functions** and the `main()` pattern

---

### 🧪 Code Used

```python
# Treasure Island Game
# A simple text-based adventure game

def main():
    print("Welcome to Treasure Island")
    print("Your mission is to find the treasure.")
    print("You are at a cross road. Where do you want to go?")
    print("Type 'left' or 'right'")
    choice1 = input().lower()

    if choice1 != "left":
        print("You fell into a hole. Game Over.")
    else:
        print("You come to a lake. There is an island in the middle of the lake.")
        print("Type 'wait' to wait for a boat. Type 'swim' to swim across.")
        choice2 = input().lower()

        if choice2 != "wait":
            print("You get attacked by an angry trout. Game Over.")
        else:
            print("You arrive at the island unharmed.")
            print("There is a house with 3 doors: red, yellow, and blue.")
            print("Which colour do you choose?")
            choice3 = input().lower()

            if choice3 == "red":
                print("Burned by fire. Game Over!")
            elif choice3 == "blue":
                print("Eaten by beasts. Game Over!")
            elif choice3 == "yellow":
                print("You found the treasure! You Win!")
            else:
                print("Game Over!")

if __name__ == "__main__":
    main()
```

### 🧩 Sample Gameplay
```bash
Welcome to Treasure Island
Your mission is to find the treasure.
You are at a cross road. Where do you want to go?
Type 'left' or 'right'
> left
You come to a lake. There is an island in the middle of the lake.
Type 'wait' to wait for a boat. Type 'swim' to swim across.
> wait
You arrive at the island unharmed.
There is a house with 3 doors: red, yellow, and blue.
Which colour do you choose?
> yellow
You found the treasure! You Win!
```

### 📌 Highlights
✅ Use of nested if conditions
✅ Handling different user inputs gracefully
✅ Creating engaging user experience with simple print statements
✅ Practicing fundamental logic building for beginner programmers

📍 Check out my full 100 Days of Python journey in the main repository 