# Generated by Django 5.1.3 on 2024-11-09 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter_analytics', '0003_voter_v20state_voter_v21primary_voter_v21town_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='date_of_birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='voter',
            name='date_of_registration',
            field=models.DateField(),
        ),
    ]