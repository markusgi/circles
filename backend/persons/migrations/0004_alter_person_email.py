# Generated by Django 3.2 on 2021-04-11 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_auto_20210411_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=60, unique=True, verbose_name='e-mail'),
        ),
    ]
