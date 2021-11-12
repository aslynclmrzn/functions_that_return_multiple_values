# Task: Redo the programs on assignment2 but now with functions that return multiple values (move all user inputs in one function)
# Define usersInfo() and use return command to return the multiple values in the function.
def usersInfo():
    inputName = input('Enter your name: ')
    inputAge = input ('Enter your age: ')
    inputAddress = input ('Enter your address: ')
    return inputName, inputAge, inputAddress
# Call the function for:
Name, Age, Address = usersInfo()
# Then, display the output in the following format.
print(f'Hi, My name is {Name}. I am {Age} years old and I live in {Address}.')
# Lastly, run and debug the program to make sure that there is no error.