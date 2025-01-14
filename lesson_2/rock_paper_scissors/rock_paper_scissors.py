import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f'==> {message}')

def display_winner(player, computer):
    if ((player == 'rock' and computer == 'scissors') or
        (player == 'paper' and computer == 'rock') or
        (player == 'scissors' and computer == 'paper')):
        return 'You win!'
    elif ((player == 'scissors' and computer == 'rock') or
        (player == 'rock' and computer == 'paper') or
        (player == 'paper' and computer == 'scissors')):
        return 'Computer wins!'
    else:
        return "It's a tie!"

keep_going = True

while keep_going:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input().lower()

    while choice not in VALID_CHOICES:
        prompt("Invalid choice, please enter either 'rock', 'paper' or 'scissors'")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose {choice}, computer chose {computer_choice}.')

    prompt(display_winner(choice, computer_choice))

    prompt('Do you want to play again? (y/n)')
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt('Invalid input, please try again (y/n)')
        answer = input().lower()

    if answer[0] == 'n':
        keep_going = False