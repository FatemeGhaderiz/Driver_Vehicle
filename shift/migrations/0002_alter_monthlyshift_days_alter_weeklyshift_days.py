# Generated by Django 5.0.2 on 2024-02-23 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shift', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyshift',
            name='days',
            field=models.CharField(max_length=61),
        ),
        migrations.AlterField(
            model_name='weeklyshift',
            name='days',
            field=models.CharField(max_length=13),
        ),
    ]
