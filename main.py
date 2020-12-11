import random

def play():
    user = input("Whats your choice??? 'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'Its a tie'


    if is_winner(user, computer):
        return 'You Won!!'

    return 'You lost, Better luck next time'


def is_winner(player, opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())

