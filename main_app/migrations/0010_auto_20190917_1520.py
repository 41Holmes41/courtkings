# Generated by Django 2.2.3 on 2019-09-17 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='owner_points',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='rank',
            field=models.IntegerField(null=True),
        ),
    ]
