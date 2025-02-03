import json

from django.shortcuts import render
from user.models import User, Game, Feedback
from django.views.generic import DeleteView

class UserDeleteView(DeleteView):
    model = User
    success_url = '..'
    template_name = 'moderator/user_delete.html'

# Create your views here.
def show_index(request):
    return render(request, "moderator/index.html")

def show_users(request):
    users = User.objects.all()
    return render(request, "moderator/user.html", {"users":users})

def show_shop(request):
    games = Game.objects.all()
    return render(request, "moderator/game.html", {"games":games})

def save_users_to_file(request):
    users = User.objects.all()

    data = {
        "users": [
            {
                "username": user.username,
                "name": user.name,
                "surname": user.surname,
                "phone_number": user.phone_number,
                "email": user.email,
                "count_of_games": user.count_of_games,
                "bought_games": user.bought_games
            } for user in users
        ]
    }
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
    return render(request, "moderator/save_to_file.html")


