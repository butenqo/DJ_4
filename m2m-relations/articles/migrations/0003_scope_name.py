# Generated by Django 4.2 on 2023-05-22 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_scope_article_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='scope',
            name='name',
            field=models.CharField(max_length=123, null=True),
        ),
    ]