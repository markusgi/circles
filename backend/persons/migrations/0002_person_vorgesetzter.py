# Generated by Django 3.2 on 2021-04-11 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='vorgesetzter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='persons.person', verbose_name='vorgesetzter'),
        ),
    ]