import random

# VALID_CHOICES = ['r', 'p', 'sc', 'l', 'sp']

VALID_CHOICES_DICT = {
    'r' : 'rock',
    'p' : 'paper',
    'sc': 'scissors',
    'l' : 'lizard',
    'sp': 'spock'
}

VALID_CHOICES = ", ".join(list(f'{key} = {value}' 
                           for (key, value) in VALID_CHOICES_DICT.items()))

def prompt(message):
    print(f'==> {message}')

def display_winner(player, computer):
    if ((player == 'rock' and
         (computer == 'scissors' or computer == 'lizard')) or
        (player == 'paper' and
         (computer == 'rock' or computer == 'spock')) or
        (player == 'scissors' and
         (computer == 'paper' or computer == 'lizard')) or
        (player == 'lizard' and
         (computer == 'spock' or computer == 'paper')) or
        (player == 'spock' and
         (computer == 'scissors' or computer == 'rock'))):
        return 'You win!'
    
    elif ((player == 'scissors' and
           (computer == 'rock' or computer == 'spock')) or
        (player == 'rock' and
         (computer == 'paper' or computer == 'spock')) or
        (player == 'paper' and
         (computer == 'scissors' or computer == 'lizard')) or
         (player == 'lizard' and
          (computer == 'scissors' or computer == 'rock')) or
          (player == 'spock' and
           (computer == 'paper' or computer == 'lizard'))):
        return 'Computer wins!'
    
    else:
        return "It's a tie!"

keep_going = True

while keep_going:
    prompt('Choose one: '
           f'{VALID_CHOICES}')
    
    choice = input().lower()

    while choice not in VALID_CHOICES_DICT and\
        choice not in VALID_CHOICES_DICT.values():

        prompt("Invalid choice, please try again\n"
               f"Your choices are: {VALID_CHOICES}")
        choice = input()

    if len(choice) <= 2:
        choice = VALID_CHOICES_DICT[choice]
    
    computer_choice = random.choice([value for value in VALID_CHOICES_DICT.values()])

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