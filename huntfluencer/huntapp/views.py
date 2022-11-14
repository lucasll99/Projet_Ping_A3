from django.http import HttpResponse
from django.shortcuts import render # traite de la génération HTML en utilisant des garabits et des données
from huntapp.models import Influenceur,Question,Reponse # importation de nos tables, qui sont en fait des objets. Les méthodes de ces
def index(request):

    # ici on peut charger nos objets ici de models (utile à la fois pour le formulaire, ainsi que pour l'affichage des résultats au client)
    context = {

    }
    return render(request, 'index.html', context=context)
    #return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>") ### Une vue est une fonction qui traite une requête HTTP, extrait des données de la base de données et les restitue dans une page HTML à l'aide d'une réponse HTTP que le navigateur mettra en forme pour l'utilisateur. 