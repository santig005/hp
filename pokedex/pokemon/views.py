from django.shortcuts import render
from .poke_api import fetch_pokemon_data

def dashboard(request):
    all_pokemon = fetch_pokemon_data()
    
    # Definimos cada una de las listas de Pokemon según los filtros solicitados por el profesor Oak
    filtered_weight = [p for p in all_pokemon if 30 < p["weight"] < 80]
    grass_type = [p for p in all_pokemon if "grass" in p["types"]]
    flying_type = [p for p in all_pokemon if "flying" in p["types"] and p["height"] > 10]
    
    context = {
        "all_pokemon": all_pokemon,
        "filtered_weight": filtered_weight,
        "grass_type": grass_type,
        "flying_type": flying_type,
    }
    return render(request, "dashboard.html", context)