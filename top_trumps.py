# This program simulates a Top Trumps card game

import random

import requests

import colorama
from colorama import Fore
colorama.init(autoreset=True)


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
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


pokemon1_stats = random_pokemon()
pokemon2_stats = random_pokemon()


def choose_pokemon():
  # added .capitalize() to names (Eduarda)
  # added print statements so player can see stats of each pokemon (Eduarda)
  
  my_pokemon1 = random_pokemon()
  print(Fore.MAGENTA + 'You were given {}'.format(my_pokemon1['name'].capitalize())) 
  print("Stats:")
  for stat_name, stat_value in pokemon1_stats.items():
    print(f"{stat_name.capitalize()}: {stat_value}")
    
  my_pokemon2 = random_pokemon()
  print(Fore.MAGENTA + 'You were given {}'.format(my_pokemon2['name'].capitalize()))
  for stat_name, stat_value in pokemon2_stats.items():
    print(f"{stat_name.capitalize()}: {stat_value}")

  my_choice = int(input('which pokemon do you want to choose? (1 or 2)'))
  if my_choice == 1:
      return my_pokemon1
  elif my_choice == 2:
      return my_pokemon2
  else:
      print("Invalid choice")
      return choose_pokemon() # Prompt again for a valid choice
  
my_choice = choose_pokemon()
print(f'Pokemon chosen: {my_choice}')


def run():
    chosen_pokemon = choose_pokemon()

    stat_choice = input(Fore.BLUE + 'Which stat do you want to use? (id, height, weight, base_experience) ').lower()

    opponent_pokemon_stats = random_pokemon()
  
    opponent_pokemon = random_pokemon()
    print(Fore.RED + 'The opponent chose {}'.format(opponent_pokemon['name']))
    # added print statements so player can see stats opponent pokemon (Eduarda)
    # there seems to be a logical error happening, where the greater stat isn't winning (Eduarda)
    print("Stats:")
    for stat_name, stat_value in opponent_pokemon_stats.items():
      print(f"{stat_name.capitalize()}: {stat_value}")

    my_stat = chosen_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]
    if my_stat > opponent_stat:
        print('You Win!')
    elif my_stat < opponent_stat:
        print('You Lose!')
    else:
        print('Draw!')
    
    # added print statements so we can see which stats are being compared (Eduarda)
    # the computer isn't comparing the chosen stats (Eduarda)
    print(f'My stat: {my_stat}')
    print(f'Opponent stat: {opponent_stat}')

    print('The stat choice is:', stat_choice)
    print('The stat value is:')
    
run()




