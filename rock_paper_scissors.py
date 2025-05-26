import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    user_input = input("Enter rock, paper, or scissors: ").lower()
    while user_input not in choices:
        user_input = input("Invalid choice. Enter rock, paper, or scissors: ").lower()
    return user_input

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user = get_user_choice()
    computer = get_computer_choice()
    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")
    print(determine_winner(user, computer))

if __name__ == "__main__":
    play_game()
