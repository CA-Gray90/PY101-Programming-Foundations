import random
import os
import time
import json

with open('messages.json', 'r') as file:
    MESSAGES = json.load(file)

with open('game_dicts.json', 'r') as file:
    GAME_DICTS = json.load(file)

VALID_CHOICES_DICT = GAME_DICTS["valid_choices_dict"]

VALID_CHOICES = ", ".join(list(f'"{key}" for {value}'
                           for (key, value) in VALID_CHOICES_DICT.items()))

WINNING_COMBOS = GAME_DICTS["winning_combos"]

WINNING_METHOD = GAME_DICTS["winning_method"]

def prompt(message):
    print(f'==> {message}')

def main_game_title():
    print(MESSAGES["main_game_title"].center(79, '*'))
    print()

def display_welcome():
    prompt(MESSAGES["welcome_title"])
    prompt(MESSAGES["welcome_phrase"])
    
def explain_rules():
    prompt(MESSAGES["rules_title"])
    print()
    print(MESSAGES["rules"])
    print()
    prompt(MESSAGES["rules_goodluck"])

def display_countdown():
    print()
    for phrase in MESSAGES["countdown_phrases"]:
        print(phrase)
        time.sleep(0.6)
    print()

def enter_to_continue():
    print()
    prompt(MESSAGES["hit_enter_message"])
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
    prompt(f'{MESSAGES["choose_weapon"]}'
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

def display_winner(winner):
    if winner == 'player':
        prompt(MESSAGES["you_win"])
    elif winner == 'computer':
        prompt(MESSAGES["computer_wins"])
    else:
        prompt(MESSAGES["its_tie"])

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

def play_match():
    while True:
        player_choice = get_player_choice()

        while invalid_choice(player_choice):
            prompt(f'{MESSAGES["invalid_choice"]} {VALID_CHOICES}')

            player_choice = input()

        player_choice = de_abbreviate_choice(player_choice)
        computer_choice = get_computer_choice()

        display_countdown()

        prompt(f'{MESSAGES["you_chose"]} {player_choice.capitalize()}, '
               f'{MESSAGES["computer_chose"]} {computer_choice.capitalize()}.')

        winner = get_winner(player_choice, computer_choice)

        display_winning_method(player_choice, computer_choice, winner)
        return winner

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
            prompt(MESSAGES["redo_match"])

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
    prompt(MESSAGES["game_over"])
    if GRAND_WINNER == 'player':
        prompt(MESSAGES["grand_winner_player"])
        prompt(MESSAGES["ai_quip"])
        print()
    else:
        prompt(MESSAGES["grand_winner_computer"])
        prompt(MESSAGES["job_quip"])
        print()

def ask_play_again():
    prompt(MESSAGES["play_again"])
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            return answer

        prompt(MESSAGES["invalid_yes_no"])
        answer = input().lower()

def exit_game(answer):
    if answer[0] == 'n':
        return True
    else:
        prompt(MESSAGES["restarting"])
        for number in '321':
            print(number)
            time.sleep(1)

        os.system('clear')
        return False

def main():
    os.system('clear')

    main_game_title()
    display_welcome()
    enter_to_continue()
    main_game_title()
    explain_rules()
    enter_to_continue()

    main_game_start = True

    while main_game_start:
        GRAND_WINNER = play_main_game()

        display_end_game(GRAND_WINNER)

        user_answer = ask_play_again()

        main_game_start = not exit_game(user_answer)

    prompt(MESSAGES["program_end"])
    time.sleep(0.5)

main()
# TODO:
# Pylint