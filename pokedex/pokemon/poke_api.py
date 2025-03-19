import requests

def fetch_pokemon_data():
    pokemon_list = []
    for id in range(1, 51):
        # Hacer una petición GET a la API de Pokemon
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
        if response.status_code == 200:
            data = response.json()
            pokemon = {
                "id": data["id"],
                "name": data["name"],
                "types": [t["type"]["name"] for t in data["types"]],
                "height": data["height"],
                "weight": data["weight"],
                "reversed_name": data["name"][::-1]  # Nombre invertido
            }
            # Agregar el diccionario a la lista de Pokemon
            pokemon_list.append(pokemon)
    return pokemon_list