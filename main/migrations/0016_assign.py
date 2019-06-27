# Generated by Django 2.2.1 on 2019-06-26 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20190608_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(choices=[('101', '101'), ('102', '102'), ('103', '103'), ('104', '104'), ('105', '105'), ('106', '106'), ('107', '107'), ('118', '118'), ('119', '119')], max_length=10, verbose_name='room')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=15, verbose_name='day')),
                ('time_slots', models.CharField(choices=[('8:00 - 8:45', '8:00 - 8:45'), ('8:55 - 9:40', '8:55 - 9:40'), ('9:50 - 10:35', '9:50 - 10:35'), ('10:45 - 11:30', '10:45 - 11:30'), ('11:40 - 12:25', '11:40 - 12:25'), ('12:35 - 13:20', '12:35 - 13:20'), ('13:30 - 14:15', '13:30 - 14:15'), ('14:25 - 15:10', '14:25 - 15:10'), ('15:20 - 16:05', '15:20 - 16:05'), ('16:15 - 17:00', '16:15 - 17:00'), ('17:10 - 17:55', '17:10 - 17:55')], default=('8:00 - 8:45', '8:00 - 8:45'), max_length=13, verbose_name='time slot')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='assign_set', to='main.Lesson', verbose_name='lesson')),
            ],
            options={
                'verbose_name': 'Assign',
                'verbose_name_plural': 'Assigns',
            },
        ),
    ]
