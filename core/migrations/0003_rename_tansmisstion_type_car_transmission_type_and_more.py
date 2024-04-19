# Generated by Django 5.0.4 on 2024-04-19 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_car"),
    ]

    operations = [
        migrations.RenameField(
            model_name="car",
            old_name="tansmisstion_type",
            new_name="transmission_type",
        ),
        migrations.AddField(
            model_name="car",
            name="color",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="car",
            name="available_for_auction",
            field=models.BooleanField(default=False),
        ),
    ]
