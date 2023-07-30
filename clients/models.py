from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    genders = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина')
    ]

    email = models.EmailField.unique
    full_name = models.CharField(max_length=150, **NULLABLE, verbose_name='Полное имя')
    comment = models.TextField(max_length=500, **NULLABLE, verbose_name='Комментарии')
    gender = models.CharField(max_length=1, choices=genders, default=MALE, **NULLABLE, verbose_name='Пол')
    age = models.IntegerField(**NULLABLE)

    def __str__(self):
        if self.gender == self.MALE:
            return f'Клиент - {self.full_name}'
        else:
            return f'Клиентка - {self.full_name}'

    class Meta:
        verbose_name = 'Клиент'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Клиенты'  # Настройка для наименования набора объектов
        ordering = ['full_name']
