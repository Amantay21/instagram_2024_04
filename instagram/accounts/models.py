from django.db import models

GENDER = [
    ('male', 'Мужчина'), ('female', 'Женщина')
]


class User(models.Model):
    login = models.CharField(max_length=200, verbose_name="Логин", unique=True)
    email = models.EmailField(max_length=400, verbose_name="Электронная почта")
    avatar = models.CharField(max_length=40000, verbose_name="Аватар")
    password = models.CharField(max_length=400, verbose_name="Пароль")
    name = models.CharField(max_length=400, null=True, blank=True, verbose_name="Имя пользователя")
    user_info = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Информация о пользователе")
    phone_number = models.CharField(max_length=15, null=True, blank=True, verbose_name="Номер пользователя")
    gender = models.CharField(max_length=400, null=True, blank=True, choices=GENDER, verbose_name="Пол пользователя")
