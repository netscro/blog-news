# Generated by Django 3.2 on 2021-04-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_auto_20210414_1438"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, upload_to=""),
        ),
    ]
