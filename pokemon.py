from bs4 import BeautifulSoup
import requests


url = "https://pokemondb.net/pokedex/all"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html")

# Assign typing weaknesses
typings = {
    "Normal":   {"weak": ["Fighting"], "resist": [], "immune": ["Ghost"]},
    "Fire":     {"weak": ["Water", "Ground", "Rock"], "resist": ["Fire", "Grass", "Ice", "Bug", "Steel", "Fairy"], "immune": []},
    "Water":    {"weak": ["Grass", "Electric"], "resist": ["Fire", "Water", "Ice", "Steel"], "immune": []},
    "Electric": {"weak": ["Ground"], "resist": ["Electric", "Flying", "Steel"], "immune": []},
    "Grass":    {"weak": ["Fire", "Ice", "Poison", "Flying", "Bug"], "resist": ["Water", "Electric", "Grass", "Ground"], "immune": []},
    "Ice":      {"weak": ["Fire", "Fighting", "Rock", "Steel"], "resist": ["Ice"], "immune":[]},
    "Fighting": {"weak": ["Flying", "Psychic", "Fairy"], "resist": ["Bug", "Rock", "Dark"], "immune": []},
    "Poison":   {"weak": ["Ground", "Psychic"], "resist": ["Grass", "Fighting", "Poison", "Bug", "Fairy"], "immune":[]},
    "Ground":   {"weak": ["Water", "Grass", "Ice"], "resist": ["Posion", "Rock"], "immune": ["Electric"]},
    "Flying":   {"weak": ["Electric", "Ice", "Rock"], "resist": ["Grass", "Fighting", "Bug"], "immune": ["Ground"]},
    "Psychic":  {"weak": ["Bug", "Ghost", "Dark"], "resist": ["Fighting", "Psychic"], "immune": []},
    "Bug":      {"weak": ["Fire", "Flying", "Rock"], "resist": ["Grass", "Fighting", "Ground"], "immune": []},
    "Rock":     {"weak": ["Water", "Grass", "Fighting", "Ground", "Steel"], "resist": ["Normal", "Fire", "Poison", "Flying"], "immune": []},
    "Ghost":    {"weak": ["Ghost", "Dark"], "resist": ["Poison", "Bug"], "immune": ["Normal", "Fighting"]},
    "Dragon":   {"weak": ["Ice", "Dragon", "Fairy"], "resist": ["Fire", "Water", "Electric", "Grass"], "immune": []},
    "Dark":     {"weak": ["Fighting", "Bug", "Fairy"], "resist": ["Ghost", "Dark",], "immune": ["Psychic"]},
    "Steel":    {"weak": ["Fire", "Fighting", "Ground"], "resist": ["Normal", "Grass", "Ice","Flying", "Psychic", "Bug", "Rock", "Dragon", "Steel", "Fairy"], "immune": ["Poison"]},
    "Fairy":    {"weak": ["Poison", "Steel"], "resist": ["Fighting", "Bug", "Dark"], "immune": ["Dragon"]},
}
# Set up a way for the pokemon to be stored

class pokedex:
    def __init__(self, dexnum, name, types, stats):
        self.dexnum = dexnum
        self.name = name
        self.types = types
        self.stats = stats
# Figure out how to make weaknesses
    def weakness_finder(self):
        weaknesses = set()
        resistances = set()
        immunites = set()

        for pokemon in self.types:
            if pokemon in typings:
                weaknesses.update(typings[pokemon]["weak"])
                resistances.update(typings[pokemon]["resist"])
                immunites.update(typings[pokemon]["immune"])

        weaknesses -= resistances
        weaknesses -= immunites


# Figure out how to put pokemon in the pokedex class established earlier

soup.find_all("a")

pokemans = []

pokemans = soup.text

for pokemans in pokedex:
    s

#Get user input to search with later
search = input("What pokemon do you want to look for ")

print(pokemans)