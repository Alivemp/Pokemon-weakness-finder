import json
import requests

# Assign typing weaknesses
typings = {
    "normal":   {"weak": ["fighting"], "resist": [], "immune": ["ghost"]},
    "fire":     {"weak": ["water", "ground", "rock"], "resist": ["fire", "grass", "ice", "bug", "steel", "fairy"], "immune": []},
    "water":    {"weak": ["grass", "electric"], "resist": ["fire", "water", "ice", "steel"], "immune": []},
    "electric": {"weak": ["ground"], "resist": ["electric", "flying", "steel"], "immune": []},
    "grass":    {"weak": ["fire", "ice", "poison", "flying", "bug"], "resist": ["water", "electric", "grass", "ground"], "immune": []},
    "ice":      {"weak": ["fire", "fighting", "rock", "steel"], "resist": ["ice"], "immune":[]},
    "fighting": {"weak": ["flying", "psychic", "fairy"], "resist": ["bug", "rock", "dark"], "immune": []},
    "poison":   {"weak": ["ground", "psychic"], "resist": ["grass", "fighting", "poison", "bug", "fairy"], "immune":[]},
    "ground":   {"weak": ["water", "grass", "ice"], "resist": ["poison", "rock"], "immune": ["electric"]},
    "flying":   {"weak": ["electric", "ice", "rock"], "resist": ["grass", "fighting", "bug"], "immune": ["ground"]},
    "psychic":  {"weak": ["bug", "ghost", "dark"], "resist": ["fighting", "psychic"], "immune": []},
    "bug":      {"weak": ["fire", "flying", "rock"], "resist": ["grass", "fighting", "ground"], "immune": []},
    "rock":     {"weak": ["water", "grass", "fighting", "ground", "steel"], "resist": ["normal", "fire", "poison", "flying"], "immune": []},
    "ghost":    {"weak": ["ghost", "dark"], "resist": ["poison", "bug"], "immune": ["normal", "fighting"]},
    "dragon":   {"weak": ["ice", "dragon", "fairy"], "resist": ["fire", "water", "electric", "grass"], "immune": []},
    "dark":     {"weak": ["fighting", "bug", "fairy"], "resist": ["ghost", "dark",], "immune": ["psychic"]},
    "steel":    {"weak": ["fire", "fighting", "ground"], "resist": ["normal", "grass", "ice", "flying", "psychic", "bug", "rock", "dragon", "steel", "fairy"], "immune": ["poison"]},
    "fairy":    {"weak": ["poison", "steel"], "resist": ["fighting", "bug", "dark"], "immune": ["dragon"]},
}
# Set up a way for the pokemon to be stored

class Pokedex:
    def __init__(self,types,):
        self.types = types

# Figure out how to make weaknesses
    def weakness_finder(self):
        types_list = self.types.split(", ")
        
        weaknesses = set()
        resistances = set()
        immunites = set()
        
        
        for pokemon in types_list:
            if pokemon in typings:
                weaknesses.update(typings[pokemon]["weak"])
                resistances.update(typings[pokemon]["resist"])
                immunites.update(typings[pokemon]["immune"])

        weaknesses -= resistances
        weaknesses -= immunites


        return list(weaknesses)
    
    def show_weakness(self) :
        if isinstance(self.types, str) :
            type_str = self.types
        else:
            type_str = ", ".join(self.types)
            
        weaknesses = self.weakness_finder()
        weaknesses_str = ", ".join(weaknesses)
        print(f"The pokemon's type is {type_str.title()}")
        print(f"The weaknesses are {weaknesses_str.title()}")




#Get user input to search with later
while True :
    search = input("What pokemon do you want to look for ")

    # Figure out how to put pokemon in the pokedex class established earlier

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{search}")

    poketype = response.json()["types"]

    poketype2 = [type_data["type"]["name"] for type_data in poketype]

    poketype3 = ", ".join([str(item) for item in poketype2])

    pokedex_instance = Pokedex(poketype3)
    pokedex_instance.show_weakness()
    end = input("Type end to end the program ")
    if end == "end":
        break