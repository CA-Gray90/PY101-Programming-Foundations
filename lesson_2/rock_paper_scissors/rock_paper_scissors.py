import random
import os
import time

VALID_CHOICES_DICT = {
    'r' : 'rock',
    'p' : 'paper',
    'sc': 'scissors',
    'l' : 'lizard',
    'sp': 'spock'
}

VALID_CHOICES = ", ".join(list(f'"{key}" for {value}'
                           for (key, value) in VALID_CHOICES_DICT.items()))

WINNING_COMBOS = {
    'rock'    : ['scissors', 'lizard'],
    'scissors': ['paper', 'lizard'],
    'paper'   : ['rock', 'spock'],
    'lizard'  : ['spock', 'paper'],
    'spock'   : ['rock', 'scissors']
}

WINNING_METHOD = {
    'rock' : {'scissors' : 'crushes', 'lizard' : 'crushes'},
    'scissors' : {'paper' : 'cuts', 'lizard' : 'decaptiates'},
    'paper' : {'rock' : 'covers', 'spock' : 'disproves'},
    'lizard' : {'spock': 'poisons', 'paper': 'eats'},
    'spock' : {'rock' : 'vapourizes', 'scissors' : 'smashes'}
}

def prompt(message):
    print(f'==> {message}')

def main_game_title():
    print('  Rock, Paper, Scissors, Lizard, Spock!  '.center(79, '*'))
    print()

def display_welcome():
    prompt('Welcome to Rock, Paper, Scissors, Lizard, Spock!')
    prompt('In this exciting game, it will be your wits against the computers.'
           ' Can you beat it?')
    
def explain_rules():
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
    prompt('All memorized? Very good! Best out of 5 wins, good luck!')

def display_countdown():
    print()
    for element in ['Here we go!!', 'Scissors!', 'Paper!', 'Rock!']:
        print(element)
        time.sleep(0.8)
    print()

def enter_to_continue():
    print()
    prompt('Hit Enter to continue...')
    input()
    os.system('clear')

def get_winner(player, computer):
    if player == computer:
        return 'tie'
    if player in WINNING_COMBOS and computer in WINNING_COMBOS[player]:
        return 'player'
    else:
        return 'computer'

def display_winning_method(player_move, computer_move, winner):
    if winner == 'player':
        prompt(f'{player_move.capitalize()} '
               f'{WINNING_METHOD[player_move][computer_move]} '
               f'{computer_move.capitalize()}!')
    elif winner == 'computer':
        prompt(f'{computer_move.capitalize()} '
               f'{WINNING_METHOD[computer_move][player_move]} '
               f'{player_move.capitalize()}!')
        
def get_player_choice():
    prompt('Choose your weapon: '
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

        display_countdown()

        prompt(f'You chose {player_choice.capitalize()}, '
               f'computer chose {computer_choice.capitalize()}.')

        winner = get_winner(player_choice, computer_choice)

        display_winning_method(player_choice, computer_choice, winner)

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
    print('*' + \
          f'{PADDING}Player: {player_score}'.ljust(INNER_WIDTH, ' ') + '*')
    print('*' + \
          f'{PADDING}Computer: {computer_score}'.ljust(INNER_WIDTH, ' ') + '*')
    print(OUTER_BORDER)

def play_main_game():
    winner_list = []
    scores = {
        'player' : 0,
        'computer' : 0
    }

    while True:
        main_game_title()

        display_scoreboard(scores['player'], scores['computer'])
        print()
        match_winner = play_match()

        display_winner(match_winner)

        if match_winner != 'tie':
            winner_list.append(match_winner)
            scores[match_winner] += 1
        else:
            prompt('Redo the match.')

        game_winner = get_grand_winner(winner_list)
        if game_winner:
            return game_winner
        
        enter_to_continue()

def get_grand_winner(winner_list):
    for player in winner_list:
        if winner_list.count(player) == 3:
            return player
    return None

def display_end_game(GRAND_WINNER):
    print()
    prompt('Game Over!')
    if GRAND_WINNER == 'player':
        prompt('You won 3 matches and beat the computer. You are the '
               'Grand Winner!')
        prompt("AI won't take over the world yet.")
        print()
    else:
        prompt('The Computer won 3 matches. They are the Grand Winner!')
        prompt('It will be coming for your job next!')
        print()

def ask_play_again():
    prompt('Do you want to play again? (y/n)')
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            return answer

        prompt('Invalid input, please try again (y/n)')
        answer = input().lower()

def main():
    main_game_start = True

    os.system('clear')

    main_game_title()
    display_welcome()
    enter_to_continue()
    main_game_title()
    explain_rules()
    enter_to_continue()

    while main_game_start:
        GRAND_WINNER = play_main_game()

        display_end_game(GRAND_WINNER)

        user_answer = ask_play_again()

        if user_answer[0] == 'n':
            main_game_start = False

        prompt('Restarting in...')
        for number in '321':
            print(number)
            time.sleep(1)

        os.system('clear')

    prompt('Program Terminated.')
    time.sleep(0.5)

main()
# TODO:
# Improve end of game display