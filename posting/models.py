from django.db import models

NULLABLE = {'blank': True, 'null': True}


class MailingLog(models.Model):
    STATUS_OK = 'ok'
    STATUS_FAILED = 'failed'
    STATUSES = [(STATUS_OK, 'Успешно'),
                (STATUS_FAILED, 'Ошибка')
    ]


class Logic(models.Model):
    STATUS_OK = 'ok'
    STATUS_FAILED = 'failed'
    STATUSES = [(STATUS_OK, 'Успешно'),
                (STATUS_FAILED, 'Ошибка')
    ]

    data_time_last = models.DateTimeField(auto_now=False,
                                          auto_now_add=False,
                                          verbose_name='Дата и время последней попытки')
    status_attempts = models.CharField(max_length=20, choices=STATUSES, verbose_name='Статус попытки')
    answer_srv_mail = models.IntegerField(**NULLABLE, verbose_name='Ответ почтового сервера')

    def __str__(self):
        return f'{self.data_time_last} {self.status_attempts}, {self.answer_srv_mail}'

    class Meta:
        verbose_name = 'Логика'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Логика'  # Настройка для наименования набора объектов
        ordering = ['data_time_last']


class Posting_tuning(models.Model):
    PERIOD_DAILY = 'daily'
    PERIOD_WEEKLY = 'weekly'
    PERIOD_MONTHLY = 'monthly'

    PERIODS = [(PERIOD_DAILY, 'Ежедневная'),
               (PERIOD_WEEKLY, 'Раз в неделю'),
               (PERIOD_MONTHLY, 'Раз в месяц'), ]

    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_DONE = 'done'

    STATUSES = [
        (STATUS_STARTED, 'Запущена'),
        (STATUS_CREATED, 'Создана'),
        (STATUS_DONE, 'Завершена')]

    data_start = models.DateTimeField(auto_now=False, auto_now_add=False,
                                      verbose_name='Дата и время рассылки')
    period = models.CharField(max_length=20, choices=PERIODS, default=PERIOD_DAILY, verbose_name='Период рассылки')
    status = models.TextField(max_length=15, choices=STATUSES, **NULLABLE, verbose_name='Статус рассылки')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.data_start} {self.period} , {self.status}'

    class Meta:
        verbose_name = 'Настройка'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Настройки'  # Настройка для наименования набора объектов
        ordering = ['data_start']


class Letter(models.Model):
    topic_letter = models.CharField(max_length=150, verbose_name='Заголовок')
    body_letter = models.TextField(**NULLABLE, verbose_name='Содержание')
    tining = models.ForeignKey(Posting_tuning, on_delete=models.CASCADE)
    logic = models.ForeignKey(Logic, on_delete=models.CASCADE, **NULLABLE)
    clients = models.ManyToManyField('clients.Client')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.topic_letter} {self.body_letter}, {self.clients}'

    class Meta:
        verbose_name = 'Письмо'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Письма'  # Настройка для наименования набора объектов
        ordering = ['topic_letter']
