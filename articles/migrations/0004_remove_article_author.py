# Generated by Django 2.2.1 on 2019-07-03 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
    ]
