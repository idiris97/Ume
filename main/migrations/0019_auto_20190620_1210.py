# Generated by Django 2.2.1 on 2019-06-20 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20190619_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assign',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='assign',
            name='start_time',
        ),
        migrations.AddField(
            model_name='assign',
            name='time_slots',
            field=models.CharField(choices=[('8:00 - 8:45', '8:00 - 8:45'), ('8:55 - 9:40', '8:55 - 9:40'), ('9:50 - 10:35', '9:50 - 10:35'), ('10:45 - 11:30', '10:45 - 11:30'), ('11:40 - 12:25', '11:40 - 12:25'), ('12:35 - 13:20', '12:35 - 13:20'), ('13:30 - 14:15', '13:30 - 14:15'), ('14:25 - 15:10', '14:25 - 15:10'), ('15:20 - 16:05', '15:20 - 16:05'), ('16:15 - 17:00', '16:15 - 17:00'), ('17:10 - 17:10', '17:10 - 17:10')], default=('8:00 - 8:45', '8:00 - 8:45'), max_length=5, verbose_name='time slot'),
        ),
    ]