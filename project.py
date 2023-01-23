import requests

while True:
    poke_search = input("Search for a Pokemon: ")
    poke_search = poke_search.lower()

    req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke_search}")
    if req.status_code == 200:
        pokemon = req.json()
        print("Pokemon name is:", pokemon['name'])
        print("Pokemon height is:", pokemon['height'])
        print("Pokemon base experience is:", pokemon['base_experience'])
        for ability in pokemon['abilities']:
            print("Pokemon abilities are:", ability['ability']['name'])
    else:
        print("Pokemon not found!")