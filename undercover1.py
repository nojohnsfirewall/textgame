#this is a silly text game

print('U n d e r c o v e r : R P G ')
playerName = input('To start, enter your name, Agent.')
output_text= 'Good luck, Agent {}.'.format(playerName)
print(output_text)
input('Press Enter to Continue')

print('You approach the enemy base.')
print('Your mission is to infiltrate, and assassinate the military officer.')
input('(Press Enter to Continue)')

print('If the element of surprise is lost, you will prematurely retire.')
input('(Press Enter to Continue)')

print('Make your decisions with A or B')
input('(Press Enter to Continue)')

print('Mission START')
input('(Press Enter to continue)')

print('Foreign Soil, 1984.\nThere are a couple of different ways to approach the compound.')
choice=None             #reformatted lingo of option code, but hit a wall. posted to show progress. prints are simplistic to fill space.
while choice== None:
    choice = input('Which do you choose?\nA)The the dark cold channel into the sewers.\nB)Advance to the guardpost ahead ')
    if choice == 'A':
        print('You slip into your wet suit, and power on your SeaGlide.')
    elif choice == 'B':
        print('You get closer to the guard post...\nYou peer at the guard through your binoculars.')
    else:
        input:('Please choose with \'A\' or \'B\' ')
        choice=None
