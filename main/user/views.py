from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_index(request):
    return render(request, "user/index.html")

def show_account(request):
    return render(request, "user/account.html")

def show_games(request):
    return render(request, "user/games.html")