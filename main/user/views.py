from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import UserForm
from .models import Game


# Create your views here.
def show_index(request):
    return render(request, "user/index.html")

def show_account(request):
    return render(request, "user/account.html")

def show_games(request):
    return render(request, "user/games.html")

def show_community(request):
    return render(request, "user/community.html")

def show_shop(request):
    games = Game.objects.all()
    return render(request, "user/shop.html", {'games':games})

def show_login(request):
    return render(request, "user/login.html")

def show_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = UserForm()
    data = {'form': form}
    return render(request, "user/create.html", data)