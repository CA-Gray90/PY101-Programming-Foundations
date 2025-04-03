# Randomly picks a topic from a selection of topics. You can save a rating (how
# well you know that topic) of 1 - 4. You can also save the topic to a viewed
# list so that you can choose to skip that topic later if you wish.

import random
import json
import os
import time

with open('topics_v2.json', 'r') as file:
    topics_dict = json.load(file)

with open('viewed_list.json', 'r') as file:
    viewed_list = list(json.load(file))

RATINGS_CHOICES = '1111111222334'

CURRENT_MODULE = 'PY101'

def get_number_of_topics(topic_dict):
    total = []

    for topic in topic_dict:
        total.append(len(topic_dict[topic]))

    return sum(total)

def prompt(text):
    print(f'--> {text}')

def display_welcome():
    os.system('clear')
    prompt(f'** Welcome to the {CURRENT_MODULE} Revision topic Generator! **')
    print()

def get_random_topic():
    while True:
        random_rating_choice = random.choice(RATINGS_CHOICES)

        if topics_dict[random_rating_choice]:
            random_topic = random.choice(topics_dict[random_rating_choice])
            break
    return random_topic

def bannerize(text):
    banner_len = len(text) + 6
    print(f'  {banner_len * '*'}')
    print(f'  |{(banner_len - 2) * ' '}|')
    print(f'  |  {text}  |')
    print(f'  |{(banner_len - 2) * ' '}|')
    print(f'  {banner_len * '*'}')

def display_topic(topic):
    prompt('Here is your randomly chosen topic for today:')
    print()
    bannerize(topic)
    print()

def skip_topic(topic, viewed):
    if topic in viewed:
        prompt('This topic has been saved to the viewed list,'
               ' would you like to skip and choose another? y/n')
        return yes_or_no()
    return None

def display_instructions():
    prompt('Write out what you can remember about this topic, or ask LSBot '
           'for 3 questions related to this topic.\nAsk LSBot to review your '
           'explanations or code.')
    print()

def get_user_rating():
    prompt('How would you rate your knowledge of the topic?\n'
        '1 - Poor, 2 - Basic, 3 - Good, 4 - Excellent')
    user_rating = input()

    while True:
        if user_rating in ['1', '2', '3', '4']:
            break

        prompt('Please enter a number from 1 to 4')
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
        prompt('Saving...')
        time.sleep(0.5)

        with open('topics_v2.json' , 'w') as file:
            json.dump(topics_dict, file)

def add_to_viewed_list(topic):
    if topic not in viewed_list:
        prompt('Topic added to viewed list...')
        viewed_list.append(topic)

        with open('viewed_list.json', 'w') as file:
            json.dump(viewed_list, file)

        time.sleep(0.5)

def get_topic_rating(topic, topics_dict):
    for rating in topics_dict.keys():
        if topic in topics_dict[rating]:
            return rating
    return None

def get_topic_length(viewed_list):
    if len(viewed_list) > 1:
            max_topic_length = len(viewed_list[0])
            for item in viewed_list[1:]:
                if len(item) > max_topic_length:
                    max_topic_length = len(item) + 3
                    return max_topic_length
    else:
        return len(viewed_list[0]) + 3

def display_viewed_list(viewed, num_of_topics, topic_dict):
    prompt('Do you wish to display the Viewed List of topics? y/n')
    
    if yes_or_no():
        max_topic_length = get_topic_length(viewed)

        print(f'- TOPICS{' ' * (max_topic_length - 6)}RATING')

        for item in viewed:
            item_rating = get_topic_rating(item, topic_dict)
            print(f'- {item}{'.' * (max_topic_length - len(item))}'
                          f'  {item_rating}')
        
        print(f'[{len(viewed)} / {num_of_topics}]')

    print()

def empty_view_list(viewed_list, num_of_topics):
    if len(viewed_list) == num_of_topics:
        prompt('You have viewed all topics, would you like to empty the viewed'
               ' list? y/n')
        if yes_or_no():
            prompt('WARNING. This will permanently empty the viewed list.'
                   ' Continue? y/n')
            if yes_or_no():
                viewed_list.clear()
                with open('viewed_list.json', 'w') as file:
                    json.dump(viewed_list, file)

def main():
    while True:
        number_of_topics = get_number_of_topics(topics_dict)
        display_welcome()
        empty_view_list(viewed_list, number_of_topics)
        while True:
            os.system('clear')
            chosen_topic = get_random_topic()
            display_topic(chosen_topic)
            if not skip_topic(chosen_topic, viewed_list):
                break

        display_instructions()
        user_rating = get_user_rating()
        save_to_json(chosen_topic, user_rating, topics_dict)
        add_to_viewed_list(chosen_topic)
        display_viewed_list(viewed_list, number_of_topics, topics_dict)
        if not try_again():
            break

main()