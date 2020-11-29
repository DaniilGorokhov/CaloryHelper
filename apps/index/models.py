from django.db import models


class User(models.Model):
    login = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=25)
    email = models.CharField(max_length=35)
    phone = models.CharField(max_length=17)
    fio = models.CharField(max_length=100)

    def __str__(self):
        return self.login


class UserHistory(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    foodName = models.CharField(max_length=50)
    foodDescription = models.CharField(max_length=50)
