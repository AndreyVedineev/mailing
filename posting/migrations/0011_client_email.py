# Generated by Django 4.2.3 on 2023-07-29 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0010_client_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(default=1, max_length=254, unique=True, verbose_name='Почта'),
            preserve_default=False,
        ),
    ]