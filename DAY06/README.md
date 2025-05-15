# 🚀 Day 6 – Reeborg's World Maze Challenge

Welcome to **Day 6** of my [100 Days of Python](https://www.udemy.com/course/100-days-of-code/) challenge!  
Today’s task focuses on solving a maze in **Reeborg’s World**, a browser-based educational environment for Python beginners.

---

## 🌟 What I Built

A simple algorithm to guide Reeborg (the robot) through a maze by checking the surrounding walls and making movement decisions.  
This logic is the foundation for solving various maze puzzles and teaches the basics of algorithms and decision-making.

---

## 🧠 Concepts Covered

- `while` loops  
- `if`, `elif`, `else` conditionals  
- Logical checks (`front_is_clear()`, `right_is_clear()`)  
- Custom function creation (e.g., `turn_right()`)

---

## 🛠️ Syntax Learned

```python
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        turn_right()
        move()
    else:
        turn_left()
```

- `not at_goal()`: Loop continues until Reeborg reaches the goal.
- `right_is_clear()` & `front_is_clear()`: Check if Reeborg can move in that direction.
- `turn_left()`: Built-in function to rotate the robot.
- `turn_right()`: Custom helper function using `turn_left()` three times.

---

## 📌 Note

This solution currently works for one specific maze layout.  
As a beginner, I am not debugging or covering all edge cases yet.  
Once I get more comfortable, I’ll improve this and upload solutions for more puzzles!

---

## 📅 Progress

✅ Completed the basic maze logic  
🔜 Plan to enhance this solution with more flexibility and handle other scenarios

---

Thanks for following along on my 100 Days of Code journey! 💻🚀

