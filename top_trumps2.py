import random

import requests

import colorama
from colorama import Fore
colorama.init(autoreset=True)

def random_pokemon():
    try:
        pokemon_number = random.randint(1, 151)
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(response)
        pokemon = response.json()
        stats = {
            'name': pokemon['name'],
            'id': pokemon['id'],
            'height': pokemon['height'],
            'weight': pokemon['weight'],
            'base_experience': pokemon['base_experience']
        }
        return stats
        
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

    my_choice = int(input('which pokemon do you want to choose? (1 or 2)'))
    if my_choice == 1:
        return my_pokemon1
    elif my_choice == 2:
        return my_pokemon2
    else:
        print("Invalid choice")
        return choose_pokemon()

def run():
    chosen_pokemon = choose_pokemon()

    stat_choice = input(Fore.BLUE + 'Which stat do you want to use? (id, height, weight, base_experience) ').lower()

    opponent_pokemon_stats = random_pokemon()
    opponent_pokemon = opponent_pokemon_stats  # Use the generated stats to represent the opponent's Pokémon
    print(Fore.RED + 'The opponent chose {}'.format(opponent_pokemon['name']))
    print("Pokemon number:", opponent_pokemon_stats)
    print("Stats:")
    for stat_name, stat_value in opponent_pokemon_stats.items():
        print(f"{stat_name.capitalize()}: {stat_value}")

    my_stat = chosen_pokemon[stat_choice]
    opponent_stat = opponent_pokemon_stats[stat_choice]
    if my_stat > opponent_stat:
        print('You Win!')
    elif my_stat < opponent_stat:
        print('You Lose!')
    else:
        print('Draw!')
        
    print(f'My stat: {my_stat}')
    print(f'Opponent stat: {opponent_stat}')

    print('The stat choice is:', stat_choice)

run()

