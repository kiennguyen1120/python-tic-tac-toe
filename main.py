import random


def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x}: "))
        if guess < random_number:
            print("too low")
        elif guess > random_number:
            print("too high")

    print(f"yay,conrat {random_number}")




def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c" and low != high:
        guess = random.randint(low, high)
        feedback = input(f"is {guess} too high (h), too low(l), correct(c)??").lower()
        if feedback == "h":
            high = guess - 1
        if feedback == "l":
            low = guess + 1


    print(f"yay, {guess}")


def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors" )
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'
    if is_win(user, computer):
        return 'you won'
    
    return 'you lost'


def is_win(player, opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


