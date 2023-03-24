import random

computerwin = 0
youwin = 0
def tricky(user):
    """Computer always won"""
    if user == 'r':
        return 'p'
    if user == 'p':
        return 's'
    else:
        return 'r'

def winner(player, opponent):
    # Return True if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player =='p' and opponent == 'r'):
        return True
    else:
        return False

while True:
    user = input("What's your choice? \n 'r' for rock, 'p' for paper, 's' for scissors => ")
    # decreasing computer's change
    Chance = random.randint(1,2)
    if Chance == 1:
        computer = tricky(user)
    else:
        computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print('Tie')

    if winner(user, computer):
        youwin += 1
        print(f"Computer: {computerwin}, You: {youwin}")

    else:
        computerwin += 1
        print(f"Computer: {computerwin}, You: {youwin}")
    # When one of them reach three end the loop and print who won the game 
    if computerwin == 5 or youwin == 5:
        if computerwin > youwin:
            print("It's over. I won :-)")
            break
        else:
            print("Congratulations!! You win...")
            break
