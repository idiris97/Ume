# Generated by Django 2.2.1 on 2019-06-28 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_lesson_topics'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='image', verbose_name='image'),
        ),
    ]
