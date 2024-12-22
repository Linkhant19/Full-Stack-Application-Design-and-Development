# Generated by Django 5.1.3 on 2024-11-09 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter_analytics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='voter_score',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='voter',
            name='apartment_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='voter',
            name='precinct_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='voter',
            name='street_number',
            field=models.IntegerField(),
        ),
    ]