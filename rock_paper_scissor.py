import random

def game():
    user = input("What's your choice? (r) for rock, (p) for papar, (s) for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        print("It's a tie!!")
        return 

    if has_won(user, computer):
        print("Yay!! You  won!")
        return 
    
    print("You lose!!!")
    return 




def has_won(player, opponent):
    # return 'true' if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

game()   