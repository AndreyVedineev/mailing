# Generated by Django 4.2.3 on 2023-07-30 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('posting', '0011_client_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.AlterField(
            model_name='letter',
            name='clients',
            field=models.ManyToManyField(to='clients.client'),
        ),
    ]