# Generated by Django 4.2.6 on 2023-10-23 14:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="No_of_guests",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="menu",
            name="Inventory",
            field=models.IntegerField(),
        ),
    ]