# Generated by Django 4.1 on 2022-08-10 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Store",
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
                ("product_name", models.CharField(max_length=100)),
                ("product_content", models.TextField()),
                ("product_image", models.ImageField(upload_to="photos/%Y/%m/%d")),
                ("time_create", models.DateTimeField(auto_now_add=True)),
                ("time_update", models.DateTimeField(auto_now=True)),
                ("product_price", models.IntegerField()),
                ("is_published", models.BooleanField(default=True)),
            ],
        ),
    ]
