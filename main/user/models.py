from django.db import models


class User(models.Model):
    username = models.CharField("Username", max_length=20)
    name = models.CharField("Ім'я",max_length=20)
    surname = models.CharField("Прізвище",max_length=20)
    phone_number = models.CharField("Номер телефону", max_length=17)
    email = models.CharField("Електронна пошта", max_length=50)
    count_of_games = models.IntegerField("Куплено ігор")
    bought_games = models.TextField("Куплені ігри", max_length=1000)

    def __str__(self):
        return self.username

class Game(models.Model):
    title = models.CharField("Назва", max_length=20)
    genre = models.CharField("Жанр", max_length=15)
    description = models.TextField("Опис", max_length=200)
    price = models.IntegerField("Ціна")
    languages = models.TextField("Мови", max_length=100)
    feedbacks = models.TextField("Відгуки", max_length=1000)

    def __str__(self):
        return self.title

class Feedback(models.Model):
    title = models.CharField("Загловок", max_length=20)
    game = models.CharField("Гра", max_length=15)
    description = models.TextField("Опис", max_length=200)
    rating = models.IntegerField("Рейтинг")
    date = models.DateField("Дата")

    def __str__(self):
        return self.title


