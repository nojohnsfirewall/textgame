print('The guard is unaware of your presence.\nA. Shoot him with a silenced pistol\nB. Attempt to snap his neck')
qr = None
while True:
    qr = input('Do you A or B? ')
    if qr == ['A', 'a']:
        print('You stalk the guard, darting between bushes before rolling into a prone position from behind a boulder.\nTheshock of surprise gives you the edge, and you get the headshot.\nProblem is, his clothes are bloody, and unuseable.')
    elif qr == ['B','b']:
        print('The guard walks by some crates, a bush and a telephone pole, the width of a man, before finishing his patrol./nHe returns back to the station for some coffee.\nThe mug would never reach his lips. You snap his neck and don his outfit in disguise.')
    elif qr == '' or not ['A','a','B','b']:
        print('Please choose with A or B, not case sensitive. ')
    else:
        break
