# Generated by Django 4.1.2 on 2022-11-01 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_rename_title_article_title1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='title1',
            new_name='title',
        ),
    ]
