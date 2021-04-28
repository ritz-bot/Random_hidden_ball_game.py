def player_chek(guess,myst):
    if myst[guess]=='o':
        print("Sahi Bhai,Party")
    else:
        print("Galt")
        print(myst)

def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess=input("Number dall de bhai:")
    
    return int(guess)
    
    
from random import shuffle
def shuffle_list(myst):
    shuffle(myst)
    return myst
            
        
myt=[' ','o',' ']

mixed_up=shuffle(myt)

guess=player_guess()

player_chek(guess,myt)
