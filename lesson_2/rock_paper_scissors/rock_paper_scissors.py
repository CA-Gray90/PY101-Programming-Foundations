import random

VALID_CHOICES_DICT = {
    'r' : 'rock',
    'p' : 'paper',
    'sc': 'scissors',
    'l' : 'lizard',
    'sp': 'spock'
}

VALID_CHOICES = ", ".join(list(f'"{key}" for {value}'
                           for (key, value) in VALID_CHOICES_DICT.items()))

def prompt(message):
    print(f'==> {message}')

def get_winner(player, computer):
    if ((player == 'rock' and
         computer in ('scissors', 'lizard')) or
        (player == 'paper' and
         computer in ('rock', 'spock')) or
        (player == 'scissors' and
         computer in ('paper', 'lizard')) or
        (player == 'lizard' and
         computer in ('spock', 'paper')) or
        (player == 'spock' and
         computer in ('scissors', 'rock'))):
        return 'player'

    if ((player == 'scissors' and
           computer in ('rock', 'spock')) or
        (player == 'rock' and
         computer in ('paper', 'spock')) or
        (player == 'paper' and
         computer in ('scissors', 'lizard')) or
        (player == 'lizard' and
         computer in ('scissors', 'rock')) or
        (player == 'spock' and
         computer in ('paper', 'lizard'))):
        return 'computer'

    return 'tie'

def get_player_choice():
    prompt('Choose one: '
           f'{VALID_CHOICES}')

    choice = input().lower()
    return choice

def invalid_choice(choice):
    if choice not in VALID_CHOICES_DICT and\
        choice not in VALID_CHOICES_DICT.values():
        return True
    return False

def de_abbreviate_choice(choice):
    if len(choice) <= 2:
        return VALID_CHOICES_DICT[choice]
    return choice

def get_computer_choice():
    choice = random.choice(list(VALID_CHOICES_DICT.values()))
    return choice

def get_grand_winner(winner_list):
    for player in winner_list:
        if winner_list.count(player) == 3:
            return player
    return None

def display_winner(winner):
    if winner == 'player':
        prompt('You win!')
    elif winner == 'computer':
        prompt('Computer wins!')
    else:
        prompt("It's a tie!")

def play_match():
    while True:

        player_choice = get_player_choice()

        while invalid_choice(player_choice):
            prompt("Invalid choice, please try again\n"
                f"Your choices are: {VALID_CHOICES}")

            player_choice = input()

        player_choice = de_abbreviate_choice(player_choice)

        computer_choice = get_computer_choice()

        prompt(f'You chose {player_choice}, computer chose {computer_choice}.')

        winner = get_winner(player_choice, computer_choice)

        return winner

main_game_start = True

while main_game_start:
    winner_list = []

    while True:
        match_winner = play_match()

        display_winner(match_winner)

        if match_winner != 'tie':
            winner_list.append(match_winner)

        print(winner_list)  # Change to function that displays score that is updated each round

        GRAND_WINNER = get_grand_winner(winner_list)
        if GRAND_WINNER:
            break

    prompt(f'End of game. {GRAND_WINNER} wins')

    prompt('Do you want to play again? (y/n)')
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt('Invalid input, please try again (y/n)')
        answer = input().lower()

    if answer[0] == 'n':
        main_game_start = False

# TODO:
# display score after each match
# display which match is about to commence
# add time delays to make the game more interesting
# clear console at strategic points to keep it clean
# Improve end of game display