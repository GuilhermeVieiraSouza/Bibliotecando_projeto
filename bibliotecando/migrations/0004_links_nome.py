# Generated by Django 5.1.2 on 2024-10-20 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotecando', '0003_remove_livro_editora'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='nome',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
