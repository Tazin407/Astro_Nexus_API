# Generated by Django 5.0.3 on 2024-06-14 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_image_alter_missions_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='missions',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]