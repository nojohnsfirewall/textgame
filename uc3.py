#this is a silly text game
#tim 2019 i t b e g i n s 
#intro prints, simplistic to rough draft basic storylines. focus is on code.
# MORE COMMENTS
print('U n d e r c o v e r : R P G ')

playerName = input('To start, enter your name, Agent. ')
playerSelect = ''
output_text= 'Good luck, Agent {}.'.format(playerName)

#in every video I've seen they always write ('string ' + playerName ),
#but I p e r s o n a l l y think {}'.format() is tidier and more <ergonomic?> verbage


print(output_text.strip())
input('Press Enter to Continue')

print('You approach the enemy base.\n')
print('Your mission is to infiltrate, and assassinate the military officer.')
input('(Press Enter to Continue)\n')

print('If the element of surprise is lost, you will prematurely retire.')
input('(Press Enter to Continue)\n')

print('Make your decisions with A or B')
input('(Press Enter to Continue)\n')

print('Mission START')
input('(Press Enter to continue)\n')

def roomA():
    roomA.options = ['A','a' , 'B','b']
    print('''

kek

''')
    
def roomB():
    roomB.options = ['A','a' , 'B','b']
    print('''

derp

''')


def snakeBox():  #main menu + game set up! (Solid [!])
    snakeBox.options = ['A' , 'B']
    playerSelect =''
    while playerSelect not in snakeBox.options:

        print('''

Foreign Soil, 1984.

There are a couple of different ways to approach the compound. you can

A. try to get through the checkpoint ahead or
B. slip into the sewer system from below the compound

''')
        #clean af (awesome formatting, mom)

        playerSelect = input('How do you proceed? (A or B?): '.casefold())
    if playerSelect in '':
        return snakeBox()
        
    elif playerSelect in snakeBox.options[0]:
        roomA()
    elif playerSelect in snakeBox.options[1]:
        roomB()
    #elif playerSelect in snakeBox.options[2]:
        #roomB()
    #elif playerSelect in snakeBox.options[3]:
        #roomB() these were to test another format of code. atm obsolete
        

snakeBox()        

    #else:
        #print('Use the correct format')
        #playerSelect not in snakeBox.options #noob: do I even need this? not sure if loop is closed with elif

