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

def main_game_title():
    print('  Rock, Paper, Scissors, Lizard, Spock!  '.center(79, '*'))
    print()

def display_welcome():
    prompt('Welcome to Rock, Paper, Scissors, Lizard, Spock!')
    prompt('In this exciting game, it will be your wits against the computers.'
           ' Can you beat it?')
    print()
    prompt('Here are the rules:')
    print('\nScissors cuts Paper,\n'
            'Paper covers Rock,\n'
            'Rock crushes Lizard,\n'
            'Lizard poisons Spock,\n'
            'Spock smashes Scissors,\n'
            'Scissors decapitates Lizard,\n'
            'Lizard eats Paper,\n'
            'Paper disproves Spock,\n'
            'Spock vaporizes Rock,\n'
            'Rock crushes Scissors\n')
    prompt('All memorized? Very good! Hit Enter to begin...')

def hit_enter():
    input()

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
        return VALID_CHOICES_DICT.get(choice)
    return choice

def get_computer_choice():
    computer_choice = random.choice(list(VALID_CHOICES_DICT.values()))
    return  computer_choice

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

def display_winner(winner):
    if winner == 'player':
        prompt('You win!')
    elif winner == 'computer':
        prompt('Computer wins!')
    else:
        prompt("It's a tie!")

def display_scoreboard(player_score, computer_score):
    TITLE = 'SCOREBOARD'
    OUTER_BORDER = '*' * (len(TITLE) + 8)
    INNER_WIDTH = len(TITLE) + 6
    PADDING = ' ' * 2

    print(OUTER_BORDER)
    print('*' + TITLE.center(INNER_WIDTH, ' ') + '*')
    print('*' + ' '.center(INNER_WIDTH, ' ') + '*')
    print('*' + f'{PADDING}Player: {player_score}'.ljust(INNER_WIDTH, ' ') + '*')
    print('*' + f'{PADDING}Computer: {computer_score}'.ljust(INNER_WIDTH, ' ') + '*')
    print(OUTER_BORDER)

def get_grand_winner(winner_list):
    for player in winner_list:
        if winner_list.count(player) == 3:
            return player
    return None

main_game_start = True

while main_game_start:
    winner_list = []
    scores = {
        'player' : 0,
        'computer' : 0
    }

    main_game_title()

    while True:
        display_welcome()
        hit_enter()

        display_scoreboard(scores['player'], scores['computer'])
        print()
        match_winner = play_match()

        display_winner(match_winner)

        if match_winner != 'tie':
            winner_list.append(match_winner)
            scores[match_winner] += 1
        else:
            prompt('Redoing match...')

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
# display how player/computer won, i.e. lizard poisons spock, rock crushes
# lizard etc
# display which match is about to commence
# add time delays to make the game more interesting
# clear console at strategic points to keep it clean
# Improve end of game display
# Add a welcome and intro to game