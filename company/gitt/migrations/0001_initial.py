# Generated by Django 4.1.5 on 2023-07-17 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pname", models.CharField(max_length=50)),
                ("pemail", models.EmailField(max_length=254)),
                ("pmobile", models.CharField(max_length=50)),
                ("paddress", models.TextField()),
            ],
        ),
    ]
