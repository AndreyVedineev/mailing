# Generated by Django 4.2.3 on 2023-08-01 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='logic',
            name='status_attempts',
            field=models.CharField(choices=[('ok', 'Успешно'), ('failed', 'Ошибка')], max_length=20, verbose_name='Статус попытки'),
        ),
        migrations.AlterField(
            model_name='posting_tuning',
            name='period',
            field=models.CharField(choices=[('daily', 'Ежедневная'), ('weekly', 'Раз в неделю'), ('monthly', 'Раз в месяц')], default='daily', max_length=20, verbose_name='Период рассылки'),
        ),
        migrations.AlterField(
            model_name='posting_tuning',
            name='status',
            field=models.TextField(blank=True, choices=[('started', 'Запущена'), ('created', 'Создана'), ('done', 'Завершена')], max_length=15, null=True, verbose_name='Статус рассылки'),
        ),
    ]
