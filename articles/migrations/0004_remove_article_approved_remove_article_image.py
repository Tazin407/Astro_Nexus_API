# Generated by Django 5.0.3 on 2024-12-14 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_image_alter_missions_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
    ]