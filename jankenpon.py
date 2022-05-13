import random


def gameok(comp, player):
    if player == comp:
        return None
    elif player == 'r':
        if comp == 'p':
            return False
        elif comp == 's':
            return True
    elif player == 's':
        if comp == 'r':
            return False
        elif comp == 'p':
            return True
    elif player == 'p':
        if comp == 's':
            return False
        elif comp == 'r':
            return True


player = (input('rock(r)\npaper(p)\nscissor(s)\nplease choose something:'))
ok = random.randint(1, 3)
if ok == 1:
    comp = 'r'
elif ok == 2:
    comp = 's'
elif ok == 3:
    comp = 'p'
Um = gameok(comp, player)
if comp == 'r':
    comp = comp.replace('r', 'rock')
elif comp == 's':
    comp = comp.replace('s', 'scissor')
elif comp == 'p':
    comp = comp.replace('p', 'paper')
if player == 'r':
    player = player.replace('r', 'rock')
elif player == 's':
    player = player.replace('s', 'scissor')
elif player == 'p':
    player = player.replace('p', 'paper')
print('comp chose ', comp)
print('player chose ', player)
if Um == None:
    print('Tie')
elif Um:
    print('You win!!')
elif Um == False:
    print('You lose!')
