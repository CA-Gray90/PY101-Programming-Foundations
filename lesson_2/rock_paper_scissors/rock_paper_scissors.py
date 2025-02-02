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

GRAND_WINNER_SCORE = 3

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

def enter_to_continue():
    print()
    prompt(MESSAGES["hit_enter_message"])
    input()
    os.system('clear')

def get_player_choice():
    prompt(f'{MESSAGES["choose_weapon"]}'
           f'{VALID_CHOICES}')

    choice = input().casefold()
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

def display_ingame_countdown():
    print()
    for phrase in MESSAGES["countdown_phrases"]:
        print(phrase)
        time.sleep(0.6)
    print()

def get_winner(player, computer):
    if player == computer:
        return 'tie'
    if computer in WINNING_COMBOS[player]:
        return 'player'
    return 'computer'

def display_winning_method(winning_choice, losing_choice):
    prompt(f'{winning_choice.capitalize()} '
            f'{WINNING_METHOD[winning_choice][losing_choice]} '
            f'{losing_choice.capitalize()}!')

def display_win_message(winner):
    if winner == 'player':
        prompt(MESSAGES["you_win"])
    elif winner == 'computer':
        prompt(MESSAGES["computer_wins"])
    else:
        prompt(MESSAGES["its_tie"])

def display_scoreboard(player_score, computer_score):
    title = 'SCOREBOARD'
    outer_border = '*' * (len(title) + 8)
    inner_width = len(title) + 6
    padding = ' ' * 2

    print(outer_border)
    print('*' + title.center(inner_width, ' ') + '*')
    print('*' + ' '.center(inner_width, ' ') + '*')
    print('*' + \
          f'{padding}Player: {player_score}'.ljust(inner_width, ' ') + '*')
    print('*' + \
          f'{padding}Computer: {computer_score}'.ljust(inner_width, ' ') + '*')
    print(outer_border)

def play_match():
    player_choice = get_player_choice()

    while invalid_choice(player_choice):
        prompt(f'{MESSAGES["invalid_choice"]} {VALID_CHOICES}')
        player_choice = input().casefold()

    player_choice = de_abbreviate_choice(player_choice)

    computer_choice = get_computer_choice()

    display_ingame_countdown()

    prompt(f'{MESSAGES["you_chose"]} {player_choice.capitalize()}, '
            f'{MESSAGES["computer_chose"]} {computer_choice.capitalize()}.')

    winner = get_winner(player_choice, computer_choice)

    if winner != 'tie':
        if winner == 'player':
            display_winning_method(player_choice, computer_choice)
        else:
            display_winning_method(computer_choice, player_choice)

    return winner

def get_grand_winner(scores_dict):
    if GRAND_WINNER_SCORE in scores_dict.values():
        return 'player' if scores_dict['player'] == GRAND_WINNER_SCORE\
              else 'computer'
    return None

def play_main_game():
    scores = {
        'player' : 0,
        'computer' : 0
    }

    while True:
        main_game_title()

        display_scoreboard(scores['player'], scores['computer'])
        print()

        match_winner = play_match()

        display_win_message(match_winner)

        if match_winner != 'tie':
            scores[match_winner] += 1
        else:
            prompt(MESSAGES["redo_match"])

        game_winner = get_grand_winner(scores)
        if game_winner:
            return game_winner

        enter_to_continue()

def display_end_game(grand_winner):
    print()
    prompt(MESSAGES["game_over"])
    if grand_winner == 'player':
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
        grand_winner = play_main_game()

        display_end_game(grand_winner)

        user_answer = ask_play_again()

        main_game_start = not exit_game(user_answer)

    prompt(MESSAGES["program_end"])
    time.sleep(0.5)

main()