# Task: Redo the programs on assignment2 but now with functions that return multiple values (move all user inputs in one function)
# Create a program that will ask how many apples and oranges you want to buy.
# Note : Define the function inputApple() then use return command to return the multiple values in the function.
def inputApple():
    appleInput = int(input("How many apples you want to buy? "))
    apple = 20
    return appleInput, apple
# Note : Define the function inputOrange() then use return command to return the multiple values in the function.
def inputOrange():
    orangeInput = int(input("How many oranges you want to buy? "))
    orange = 25
    return orangeInput , orange
# Note : Define the function output(totalA) that will display the final output of the program.
def output(totalA):
    print (f'The total amount is {total}.')
# Call the function for:
appleAmount, applePrice = inputApple()
orangeAmount, orangePrice = inputOrange()
total = int(appleAmount*applePrice) + (orangeAmount*orangePrice)
output(total)
# Lastly, run and debug the program to make sure that it is working.