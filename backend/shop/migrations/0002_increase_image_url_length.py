# Increase image URL limits for ImageKit URLs.
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image_url",
            field=models.URLField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name="category",
            name="image_url",
            field=models.URLField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name="aboutpage",
            name="image_url",
            field=models.URLField(blank=True, max_length=1000),
        ),
    ]
