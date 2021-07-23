# Generated by Django 3.2.5 on 2021-07-21 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='game',
        ),
        migrations.AlterField(
            model_name='game',
            name='losers',
            field=models.ManyToManyField(blank=True, related_name='lose', to='dashboard.Score'),
        ),
        migrations.AlterField(
            model_name='game',
            name='winners',
            field=models.ManyToManyField(blank=True, related_name='win', to='dashboard.Score'),
        ),
    ]