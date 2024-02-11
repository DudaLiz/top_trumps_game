# this program simulates a Top Trumps card gamme
# player is assigned 2 cards and chooses one card and one stat to bet against computer
# highest stat wins

import random

import requests

import colorama
from colorama import Fore
colorama.init(autoreset=True)

# def random_pokemon():
#     try:
#         pokemon_number = random.randint(1, 151)
#         url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an exception for HTTP errors
#         print() # added line space
#         print(response, '\n') # added line space
#         pokemon = response.json()

#         base_stats = {}
#         for stat in pokemon['stats']:
#             stat_name = stat['stat']['name']
#             base_stats[stat_name] = stat['base_stat']

#         stats = {
#             'name': pokemon['name'],
#             'id': pokemon['id'],
#             'height': pokemon['height'],
#             'weight': pokemon['weight'],
#             'base_experience': pokemon['base_experience']
#         }

#         new_stats = {'attack': pokemon['stats'][1]['base_stat'],}
                     
#         stats.update(new_stats)

#         return stats

def random_pokemon():
    try:
        pokemon_number = random.randint(1, 151)
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print() # added line space
        print(response, '\n') # added line space
        pokemon = response.json()

        base_stats = {}
        for stat in pokemon['stats']:
            stat_name = stat['stat']['name']
            base_stats[stat_name] = stat['base_stat']

        stats = {
            'name': pokemon['name'],
            'id': pokemon['id'],
            'height': pokemon['height'],
            'weight': pokemon['weight'],
            'base_experience': pokemon['base_experience'],
            'attack': base_stats.get('attack'),
            'defense': base_stats.get('defense'),
            'special_attack': base_stats.get('special-attack'),
            'special_defense': base_stats.get('special-defense'),
            'speed': base_stats.get('speed'),
            'hp': base_stats.get('hp')
        }

        return stats
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

    
        
    except requests.exceptions.RequestException as e: 
        print("Error:", e)
        return None


def choose_pokemon():
    my_pokemon1 = random_pokemon()
    print(Fore.MAGENTA + 'You were given {}'.format(my_pokemon1['name'].capitalize())) 
    print("Stats:")
    for stat_name, stat_value in my_pokemon1.items():
        print(f"{stat_name.capitalize()}: {stat_value}")
    
    my_pokemon2 = random_pokemon()
    print(Fore.MAGENTA + 'You were given {}'.format(my_pokemon2['name'].capitalize()))
    print("Stats:")
    for stat_name, stat_value in my_pokemon2.items():
        print(f"{stat_name.capitalize()}: {stat_value}")

    print() # added line space
    # added defensive programing .strip() to avoid errors in user input - white spaces
    my_choice = int(input(Fore.MAGENTA + 'which pokemon do you want to choose? (1 or 2) ').strip()) 
    if my_choice == 1:
        return my_pokemon1
    elif my_choice == 2:
        return my_pokemon2
    else:
        print("Invalid choice")
        return choose_pokemon() # prompts user for new input

def run():
    chosen_pokemon = choose_pokemon()
    # added defensive programing .lower() and .strip() to avoid errors in user input - capitalization and white spaces
    stat_choice = input(Fore.BLUE + 'Which stat do you want to use? (id, height, weight, base_experience) ').lower().strip()

    opponent_pokemon_stats = random_pokemon()
    opponent_pokemon = opponent_pokemon_stats  # Use the generated stats to represent the opponent's Pokémon 
    print(Fore.RED + 'The opponent chose {}'.format(opponent_pokemon['name']))
    print("Stats:")
    for stat_name, stat_value in opponent_pokemon_stats.items():
        print(f"{stat_name.capitalize()}: {stat_value}")
    print() # added line space

    my_stat = chosen_pokemon[stat_choice]
    opponent_stat = opponent_pokemon_stats[stat_choice]
    if my_stat > opponent_stat:
        print(Fore.GREEN + 'You Win!')
    elif my_stat < opponent_stat:
        print(Fore.RED + 'You Lose!')
    else:
        print(Fore.CYAN + 'Draw!')

    print() # added line space
        
    print(f'My stat: {my_stat}')
    print(f'Opponent stat: {opponent_stat}')

    print('The stat choice is:', stat_choice)

run()


