# Generated by Django 4.2.3 on 2023-07-12 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="short_desc",
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
