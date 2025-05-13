# 📅 Day 2 – Tip Calculator 💸

## 📌 Project: Tip Calculator

On **Day 2**, I built a **Tip Calculator** that helps users calculate how much each person should pay when splitting a bill — including the tip.

This project takes the total bill, tip percentage, and number of people as inputs, then calculates the share for each individual.

---

### 🧠 What I Learned

- How to work with `input()` and convert values to `float`
- Removing prefixes and suffixes from strings using `removeprefix()` and `removesuffix()`
- Calculating percentages and splitting bills
- Conditional logic using `if-else`
- Function creation and calling functions from `main()`
- Rounding values using `round()`
- Printing formatted output using `f-strings`

---

### 🧪 Code Used

```python
def bill(user_bill, user_tip, user_split):
    user_bill = user_bill.removeprefix("$")
    user_bill = float(user_bill)
   
    user_tip = user_tip.removesuffix("%")
    user_tip = float(user_tip) / 100
    user_tip = user_bill + (user_tip * user_bill)
    
    user_split = float(user_split)
    if user_split == 0:
        return user_tip
    else:
        each_person = float(user_tip / user_split)
        each_person = round(each_person, 2)
        print(f"Each person should pay: ${each_person}")

def main():
    print("Welcome to the tip calculator")
    user_bill = input("What was the total bill? ")
    user_tip = input("How much tip would you like to give? 10, 12, 15? ")
    user_split = input("How many people to split the bill? ")
    bill(user_bill, user_tip, user_split)

main()
```

### 🎯 Sample Output
```bash
Welcome to the tip calculator
What was the total bill? $100
How much tip would you like to give? 15%
How many people to split the bill? 4
Each person should pay: $28.75
```

### 📘 Notes
- Used string methods like .removeprefix() and .removesuffix() to clean user input.
- Carefully handled division by zero with a condition.
- Rounded the result to 2 decimal places for currency formatting.

📍 Follow my full progress in the main repository: https://github.com/chudalnischal/100-Days-of-Python 