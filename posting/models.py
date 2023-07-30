from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Logic(models.Model):
    data_time_last = models.DateTimeField(auto_now=False,
                                          auto_now_add=False,
                                          verbose_name='Дата и время последней попытки')
    status_attempts = models.CharField(max_length=20, verbose_name='Статус попытки')
    answer_srv_mail = models.IntegerField(**NULLABLE, verbose_name='Ответ почтового сервера')

    def __str__(self):
        return f'{self.data_time_last} {self.status_attempts}, {self.answer_srv_mail}'

    class Meta:
        verbose_name = 'Логика'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Логика'  # Настройка для наименования набора объектов
        ordering = ['data_time_last']


class Posting_tuning(models.Model):
    DAY = '1'
    WEEK = '2'
    MONTH = '3'
    periods = [
        (DAY, 'раз в день'),
        (WEEK, 'раз в неделю'),
        (MONTH, 'раз в месяц')
    ]

    data_start = models.DateTimeField(auto_now=False, auto_now_add=False,
                                      verbose_name='Дата и время рассылки')
    period = models.CharField(max_length=20, choices=periods, default=DAY, verbose_name='Период рассылки')
    # period = models.TextField(verbose_name='Период рассылки')
    status = models.TextField(max_length=15, **NULLABLE, verbose_name='Статус рассылки')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.data_start} {self.period} , {self.status}'

    class Meta:
        verbose_name = 'Настройка'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Настройки'  # Настройка для наименования набора объектов
        ordering = ['data_start']


# class Client(models.Model):
#     MALE = 'M'
#     FEMALE = 'F'
#     genders = [
#         (MALE, 'Мужчина'),
#         (FEMALE, 'Женщина')
#     ]
#
#     email = models.EmailField(unique=True, verbose_name='Почта' )
#     full_name = models.CharField(max_length=150, **NULLABLE, verbose_name='Полное имя')
#     comment = models.TextField(max_length=500, **NULLABLE, verbose_name='Комментарии')
#     gender = models.CharField(max_length=1, choices=genders, default=MALE, **NULLABLE, verbose_name='Пол')
#     age = models.IntegerField(**NULLABLE)
#
#     def __str__(self):
#         if self.gender == self.MALE:
#             return f'Клиент - {self.full_name}'
#         else:
#             return f'Клиентка - {self.full_name}'
#
#     class Meta:
#         verbose_name = 'Клиент'  # Настройка для наименования одного объекта
#         verbose_name_plural = 'Клиенты'  # Настройка для наименования набора объектов
#         ordering = ['full_name']


class Letter(models.Model):
    topic_letter = models.CharField(max_length=150, verbose_name='Заголовок')
    body_letter = models.TextField(**NULLABLE, verbose_name='Содержание')
    tining = models.ForeignKey(Posting_tuning, on_delete=models.CASCADE)
    logic = models.ForeignKey(Logic, on_delete=models.CASCADE, **NULLABLE)
    clients = models.ManyToManyField('clients.Client')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.topic_letter} {self.body_letter}'

    class Meta:
        verbose_name = 'Письмо'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Письма'  # Настройка для наименования набора объектов
        ordering = ['topic_letter']


