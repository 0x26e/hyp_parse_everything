import json
import grequests
from pprint import pprint
import sys
import time
from sections.SmashHeroes.getSmashHeroes import getSmashHeroes
from sections.Quakecraft.getQuakecraft import getQuakecraft
from sections.Bedwars.getBedwars import getBedwars

# Get number of stats from nested dict/lists
def get_total_keys(data):

    if not isinstance(data, dict):
        return 0

    nested_keys = sum(get_total_keys(value) for key, value in data.items())
    return len(data) + nested_keys

# Get number of bytes from nested dict/lists
def get_total_bytes(data):

    if not isinstance(data, dict):
        return sys.getsizeof(data)

    nested_bytes = sum(get_total_keys(value) for key, value in data.items())
    return sys.getsizeof(data) + nested_bytes


# Gets all player stats
def getAllStats(url):

    # Async call to url
    resp = grequests.get(url)

    # For every response
    for data in grequests.map([resp]):

        # Load data with JSON
        data = json.loads(data.content)

        # If response successful
        if(data["success"]):

            # Set up player container
            finalized_stats = {"game_stats": {}}

            # If stats for games are present
            if "stats" in data["player"]:

                # If no game stats, add default containers
                data["player"]["stats"] = {
                    gamemode: data["player"]["stats"].get(gamemode, {})
                    for gamemode in hypixel_stats_gamemodes
                }

                # Check every game
                for gm, gm_proper in hypixel_stats_gamemodes.items():

                    # Add proper stats to proper container
                    finalized_stats["game_stats"][gm_proper[0]] = gm_proper[1](data["player"]["stats"][gm], data["player"]["achievements"])

            # If achievements are present
            if "achievements" in data["player"]:
                #stats = getAchievements()
                pass
            else:
                data["player"]["achievements"] = {}


            # Return proper stats container
            return(finalized_stats)


# Get API key from API_KEY.json
API_FILE = open("API_KEY.json", "r")
API_KEY = json.loads(API_FILE.read())["API_KEY"]

# Players for testing
known_players = {
    "Global":
    ( ("greaneye", "1fc7b5e6-c8e1-433b-a41e-7013ab0a3582"),
      ("Anchor_Falls", "d0cdf17b-f8bd-4195-a8ab-c366bd5eb7c3"), ),
    "SmashHeroes":
    ( ("Hyplex", "bec9029b-efb3-4c85-925d-f2e97640cf92"),
      ("Focus_Energy", "2de27887-dbb9-4154-8a36-029d6de5f468"), ),
    "Bedwars":
    ( ("TheCleb", "ed6dd177-717a-43b3-b17b-f02031cfac4e"), ),
    "Quake":
    ( ("Govo", "511a4cd1-138b-45b9-8d39-3680454bd6e3"),
      ("Rackals", "e2f69d3e-e11d-4870-81b6-08ed6bdf09c0"), ),
    }

# Select player for testing
player_to_test = ("Quake", 0)

# Player to test
NAME = known_players[player_to_test[0]][player_to_test[1]][0]
# UUID of player to test
UUID = known_players[player_to_test[0]][player_to_test[1]][1]

print(NAME, UUID)

# URL for Hypixel player endpoint
URL = f"https://api.hypixel.net/player?key={API_KEY}&uuid={UUID}"

# List of gamemodes
hypixel_stats_gamemodes = {
    "SuperSmash": ("smash_heroes", getSmashHeroes),
    "Bedwars": ("bedwars", getBedwars),
    "Quake": ("quake", getQuakecraft),
    }

reformed_stats = getAllStats(URL)

pprint(reformed_stats["game_stats"]["Quake"])

print("Total stats parsed: ", get_total_keys(reformed_stats))

print("Total bytes stored: ", get_total_bytes(reformed_stats))























#
