# Randomly picks a topic from a selection of topics. Briefly write about and code
# an example to demonstrate your understanding of each topic that is raised. 
# Submit the question and your answer to LSbot to get a revision.

import random
import json
import os

with open('topics.json', 'r') as file:
    topics_dict = json.load(file)

RATINGS_CHOICES = '1111111222334'

def prompt(text):
    print('--> {}'.format(text))

def get_random_topic():
    while True:
        random_rating_choice = random.choice(RATINGS_CHOICES)

        if topics_dict[random_rating_choice]:
            random_topic = random.choice(topics_dict[random_rating_choice])
            break
    return random_topic

def display_topic(topic):
    prompt('Here is your randomly chosen topic for today:')
    print()
    print('* ' * 30)
    prompt(topic)
    print('* ' * 30)
    print()

def display_instructions():
    prompt('Write out what you can remember about this topic, or ask LSBot '
           'for 5 questions related to this topic.\nAsk LSBot to review your '
           'explanations or code.')
    print()

def get_user_rating():
    prompt('How would you rate your knowledge of the topic?\n'
        '1 - Poor, 2 - Basic, 3 - Good, 4 - Excellent')
    user_rating = input()

    while True:
        if user_rating in ['1', '2', '3', '4']:
            break
        else:
            prompt('Please enter a number from 1 to 4.')
            user_rating = input()
    
    return user_rating

def yes_or_no():
    response = input().lower()
    while True:
        if response not in ['y', 'n']:
            prompt('Try again. y/n')
            response = input().lower()
        else:
            return response == 'y'

def try_again():
    prompt('Study another topic? y/n')
    return yes_or_no()

def save_to_json(topic, rating, topic_dict):
    prompt('Do you wish to save this rating to the topics file?\n'
           '(Higher rated topics are less likely to be reviewed again)\n'
           'y/n?')
    if yes_or_no():
        for rated_list in topic_dict.values():
            if topic in rated_list:
                rated_list.remove(topic)

        topic_dict[rating].append(topic)

        with open('topics.json' , 'w') as file:
            json.dump(topics_dict, file)
def main():
    while True:
        os.system('clear')  
        chosen_topic = get_random_topic()
        display_topic(chosen_topic)
        display_instructions()
        user_rating = get_user_rating()
        save_to_json(chosen_topic, user_rating, topics_dict)
        if not try_again():
            break

main()

# TODO: A way to keep track of what
# topics have been revisited already and exclude those.