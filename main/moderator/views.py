from django.shortcuts import render
from user.models import User, Game, Feedback
from django.views.generic import DeleteView, UpdateView

class UserDeleteView(DeleteView):
    model = User
    success_url = 'moderator/users'
    template_name = 'moderator/templates/moderator/user_delete.html'

# Create your views here.
def show_index(request):
    return render(request, "moderator/index.html")

def show_users(request):
    users = User.objects.all()
    return render(request, "moderator/user.html", {"users":users})

def show_shop(request):
    games = Game.objects.all()
    return render(request, "moderator/game.html", {"games":games})




def show_games(request):

    return render(request, "main/index.html")



def show_community(request):

    return render(request, "main/index.html")
