

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
        each_person = float (user_tip / user_split)
        each_person = round(each_person, 2)
        print(f"Each person should pay: ${each_person}")
        

def  main():
    print("Welcome to the tip calculator")
    user_bill = input("What was the total bill ? ")
    user_tip = input("How much tip would you like to give ? 10, 12, 15? ")
    user_split = input("How many people to split the bill? ")
    bill(user_bill, user_tip, user_split)



main()
