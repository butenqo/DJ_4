# Generated by Django 4.2 on 2023-05-22 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_remove_article_tag_scope_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scope',
            name='name',
        ),
    ]
