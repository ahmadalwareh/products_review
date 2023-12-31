# Generated by Django 4.2.6 on 2023-10-21 11:42

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):
    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
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
                ("name", models.CharField(max_length=255)),
                (
                    "image",
                    versatileimagefield.fields.VersatileImageField(
                        upload_to="images/", verbose_name="Image"
                    ),
                ),
                (
                    "image_ppoi",
                    versatileimagefield.fields.PPOIField(
                        default="0.5x0.5", editable=False, max_length=20
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ManyToManyField(related_name="products", to="reviews.image"),
        ),
    ]
