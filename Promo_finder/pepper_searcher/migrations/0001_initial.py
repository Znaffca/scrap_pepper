# Generated by Django 2.2.3 on 2019-07-14 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categories",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category_name", models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name="PepperPromo",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fullname", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=7)),
                ("url_link", models.TextField()),
                ("promo_code", models.CharField(max_length=80)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="category_id",
                        to="pepper_searcher.Categories",
                    ),
                ),
            ],
        ),
    ]
