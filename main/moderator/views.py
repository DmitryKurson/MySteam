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