# For data types, there are strings, int (if they have no decimals), floats (if they have decimals, even such as 22.0), and booleans (True or False)

# Input statements asks the user for input. In the example below, the user can type their name in the terminal. Inputs always return strings
# input('Type your name: ')
# or
# name: str = input('Type your name: ')
# print(name)

# When declaring variables, we can use underscores and numbers, upper/lowercase letters but no special characters. We also cannot start with a number
# my_variable = 3 is valid
# Also, my-Variable is not the same as my-variable. Capitalization matters



# Introduce the player to the game

player_name = input('Welcome to My Game! Enter your name to start: ')
print('Hi ' + player_name + ', nice to meet you! Allow me to briefly explain what My Game is about.')

# lower() will lowercase any input from the user
intro_prompt = input('My Game will have you choose various paths throughout your journey. Each path will have their own benefits and dangers, so choose wisely! Are you ready to begin? Yes/No: ').lower()

# We can create a variable for the condition below or we can create it inline 
# player_start = intro_prompt == 'yes' 

if intro_prompt == 'yes' or intro_prompt == 'y':
    print('Awesome! Good luck on your future endeavors, ' + player_name + '. Without any further delay, let\'s get started!')
else:
    print('Very well, come back once you are ready to take on the challenge!')