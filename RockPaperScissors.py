import random

computerwin = 0
youwin = 0

def winner(player, opponent):
    # Return True if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player =='p' and opponent == 'r'):
        return True
    else:
        return False

while True:
    user = input("What's your choice? \n 'r' for rock, 'p' for paper, 's' for scissors => ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print('Tie')

    if winner(user, computer):
        youwin += 1
        print(f"Computer: {computerwin}, You: {youwin}")

    else:
        computerwin += 1
        print(f"Computer: {computerwin}, You: {youwin}")

    if computerwin == 3 or youwin == 3:
        if computerwin > youwin:
            print("It's over. I won :-)")
            break
        else:
            print("Congratulations!! You win...")
            break
