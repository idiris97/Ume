# Generated by Django 2.2.1 on 2019-05-25 08:41

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20190524_0935'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Teacher', 'verbose_name_plural': 'Teachers'},
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='teacher',
            name='lessons',
            field=models.ManyToManyField(related_name='lesson_list', to='main.Lesson', verbose_name='lessons'),
        ),
    ]