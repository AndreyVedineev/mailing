# Generated by Django 4.2.3 on 2023-07-28 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0004_letter_logic_alter_posting_tuning_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting_tuning',
            name='status',
            field=models.TextField(blank=True, max_length=15, null=True, verbose_name='Статус рассылки'),
        ),
    ]