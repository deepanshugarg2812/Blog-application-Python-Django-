# Generated by Django 3.0.6 on 2020-05-29 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_article_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='name',
            new_name='body',
        ),
    ]
