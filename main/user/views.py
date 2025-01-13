from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .forms import UserForm
from .models import Game, User


# Create your views here.
def show_index(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, "user/index.html",{'user':user})

def show_account(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, "user/account.html",{'user':user})

def show_games(request, user_id):
    user = get_object_or_404(User, id=user_id)
    games_str = user.bought_games
    games = games_str.split(", ")
    if games[0] == "":
        games = []
    return render(request, "user/games.html", {'games':games})

def show_community(request):
    return render(request, "user/community.html")

def show_shop(request, user_id):
    user = get_object_or_404(User, id=user_id)
    all_games = Game.objects.all()
    user_games = user.bought_games
    games_to_show = []
    for i in all_games:
        if not i.title in user_games:
            games_to_show.append(i)

    if request.method == 'POST':
        game_id = request.POST.get('game_id')
        try:
            game = Game.objects.get(id=game_id)
            if user.bought_games:
                user.bought_games += (", " + game.title)
            else:
                user.bought_games = game.title
            user.count_of_games += 1
            user.save()
            return redirect('shop', user_id=user.id)
        except:
            return HttpResponse("Game not found", status=404)
    return render(request, "user/shop.html", {'games':games_to_show, 'user':user})

def show_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            return redirect('index', user_id = user.id)
        except:
            return render(request, 'user/login.html')

    return render(request, "user/login.html")

def show_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.count_of_games = 0
            user.bought_games = ""
            user.save()
            return redirect('index')
    form = UserForm()
    data = {'form': form}
    return render(request, "user/create.html", data)