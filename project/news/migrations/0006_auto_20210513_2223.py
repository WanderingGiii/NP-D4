# Generated by Django 3.2 on 2021-05-13 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_cathegory_cathegory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cathegory',
            name='cathegory',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]
