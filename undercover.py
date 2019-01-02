#this is a silly text game

print('U n d e r c o v e r : R P G ')
while True:
    query = input('Do you wish to begin?y/n: ')
    Fl = query[0].lower()
    if query == ''or not Fl in ['y','n']:
        print('Please answer with yes or no!')
    else:
        break
if Fl== 'y':
    player_name = input('What is your CodeName? ')
    print('Your CodeName is: {}'.format(player_name))
while True:
    query = input('Start? y/n: ')
    Fl = query[0].lower()
    if query == ''or not Fl in ['y','n']:
        print('Give a yay or nay somehow')
        if Fl== 'y':
            print('You approach the enemy base.')
            print('Your mission is to infiltrate, and assassinate the military officer.')
            print('How do you sneak in?')
            print('1. Slink into the sewers from the nearby channel.')
            print('2. Attempt to subdue the guard at the checkpoint ahead.')
        if Fl =='n':
            print('Please close the window. Personal data safely encrypted.')
while True:
    query = input('Select: ')
    Fl = query[0].lower()
    if query == ''or not Fl in ['1','2']:
        print('Type 1 or 2 to select choices')
        if Fl=='1':
            print('The water is warm from the summer as you stride into the dark waves.')
            print('')
            print('Your personal swimming device hums gently as it pulls you deeper.')
            print('')
            print('The fauna is nice~')
            print('')
            print('Holy shit balls batman, a squid comes out of nowhere and grabs your leg.')
            print('')
            print('You fumble to grasp your Combat Knife, but grab hold and slash the tentacle off,')
            print('releasing a cloud of dark ink and blood into the water around you.')
            print('')
            print('You travel a bit further.')
            print('')
            print('You think you have found the entrance. You push aside seaweed to reveal a latch.')
        if Fl=='2':
            print('You lay prone between some bushes, peering at the compound through your binoculars.')
            print('')
            print('You see the checkpoint just ahead, a single guard paces back and forth in front of the barrier.')
            print('')
            print('How do you eliminate the guard?')
            print('1. Marksmanship')
            print('2. Up close and personal.')
