# Generated by Django 3.2 on 2021-04-14 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0005_auto_20210414_1542"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="text",
            field=models.TextField(max_length=500, null=True),
        ),
    ]
