# Generated by Django 2.2.3 on 2019-09-16 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20190916_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_points',
            field=models.IntegerField(null=True),
        ),
    ]
