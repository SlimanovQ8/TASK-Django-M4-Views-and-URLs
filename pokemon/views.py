from django.http import HttpResponse
from django.urls import reverse
from rest_framework.generics import ListAPIView
from .models import Pokemon
from .serializers import ListSerializer

def get_pokemon(request, pokemon_id):
    poke = Pokemon.objects.get(id=pokemon_id)
    isActive = "Yes" if poke.active else "No"
    pokelist = f""" <li> Name: {poke.name} </li>
    
                 <li> Type: {poke.type}</li>
                 <li> HP: {poke.hp}</li>
                 <li> France name: {poke.name_fr}</li>
                 <li> Arabic name: {poke.name_ar}</li>
                  <li> Active: {isActive} </li>"""
    return HttpResponse(f" {pokelist} ")

def get_pokemons(request):
    pokemons = Pokemon.objects.all().values_list("name", flat=True)
    id = Pokemon.objects.all().values_list("id",)



    pokemons_list = "\n".join(f'<li> <a href="{ reverse("p", args= ("1")) }"> {q} </a> </li>' for q in pokemons)
    return HttpResponse(f"<b> {pokemons_list}</b>")

class PokeListAPIView(ListAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = ListSerializer