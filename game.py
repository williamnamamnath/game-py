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
print('Hi ' + player_name + ', nice to meet you! Allow me to briefly explain what this game is about.')

# lower() will lowercase any input from the user
intro_prompt = input('Treasure Hunt will have you depart from Clover Kingdom at the request of King William VII with a group of 10 knights in order to retrieve a rare emerald from the Land of Despair. In order to play, you will have to choose various paths throughout your mission. Each path will have their own benefits and dangers for both your mission and your team\'s stats, so choose wisely! Here are your team\'s stats: '
'My player: ' + player_name + ', '
'- Health: 100, '
'- Attack: 80, '
'- Defense: 70, '
'- Speed: 70, '
'- Stamina: 90. '
'And now, here are the stats for the 10 knights that will be accompanying you: '
'- Knights\' Health: 100, '
'- Knights\' Attack: 60, '
'- Knights\' Defense: 35, '
'- Knights\' Speed: 50, '
'- Knights\' Stamina: 60. '
'Are you ready to begin? (Yes/No): ').lower()

# We can create a variable for the condition below or we can create it inline 
# player_start = intro_prompt == 'yes' 

if intro_prompt == 'yes' or intro_prompt == 'y':
    print('Awesome! Good luck on your future endeavors, ' + player_name + '. Without any further delay, let\'s get started!')
elif intro_prompt == 'no' or intro_prompt == 'n':    
    print('Very well, come back once you are ready to take on the challenge!')
else:
    print('Sorry, this was not a valid input. Please try again.')


first_path = input('You have left Clover Kingdom and have been walking for 5 hours and you have now reached the Grand Forest. Would you like to take a break? (Yes/No): ').lower()
if first_path == 'yes' or first_path == 'y':
    print('You have decided to rest for 30 minutes. Your squad feels rejuvenated and their stats have improved. You are ready to continue your journey.')
elif first_path == 'no' or first_path == 'n':
    print('You have decided to power through as you\'d like to complete this mission as soon as possible. Your squad yearns for a quick break in order to eat, but they trust your judgement. Their stats have taken a hit.')
else:
    print('Sorry, this was not a valid input. Please try again.')

