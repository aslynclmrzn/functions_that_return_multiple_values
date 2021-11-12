# Task: Redo the programs on assignment2 but now with functions that return multiple values (move all user inputs in one function)
# Step 1: Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Note: Define the function userInput() then use return command to return the multiple values in the function.
def userInput():
    moneyAmount = int(input("Enter amount of money: "))
    priceApple = int(input("What is the price of apple? "))
    return moneyAmount, priceApple
# Step 2: Display the maximum number of apples that you can buy and the remaining money that you will have.
# Note: Define the function compute() and use return command to return the multiple values in the function.
def compute():
    total = int(amount/price)
    balance = int(amount-(total*price))
    return total, balance
# Step 3: Display the output in the following format.
def output(totalA, balanceB):
    print (f"You can buy {total} apples and your change is {balance} pesos.")
# Call the function for:
amount, price = userInput()
total, balance = compute()
output(total, balance)
# Then, run the entire program.