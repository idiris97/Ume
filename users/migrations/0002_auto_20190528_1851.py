# Generated by Django 2.2.1 on 2019-05-28 12:51

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
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
        migrations.RemoveField(
            model_name='student',
            name='curator',
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(blank=True, choices=[('UME-I', 'First course'), ('UME-II', 'Second course'), ('UME-III', 'Third course'), ('UME-IV', 'Fourth course')], max_length=7, null=True, verbose_name='course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='father',
            field=models.CharField(blank=True, max_length=55, null=True, verbose_name='father'),
        ),
        migrations.AlterField(
            model_name='student',
            name='home_address',
            field=models.TextField(blank=True, null=True, verbose_name='home address'),
        ),
        migrations.AlterField(
            model_name='student',
            name='lessons',
            field=models.ManyToManyField(related_name='student_list', to='main.Lesson', verbose_name='lessons'),
        ),
        migrations.AlterField(
            model_name='student',
            name='mother',
            field=models.CharField(blank=True, max_length=55, null=True, verbose_name='mother'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+996999999'. Up to 15 digits allowed", regex='^\\+?996?\\d{9,15}$'), django.core.validators.RegexValidator(message='Please type in the correct format.', regex='^\\+?90\\d{10, 12}$')], verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='student_profile', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='degree',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='degree'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='father',
            field=models.CharField(blank=True, max_length=55, null=True, verbose_name='father'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='home_address',
            field=models.TextField(blank=True, null=True, verbose_name='home address'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='lessons',
            field=models.ManyToManyField(related_name='lesson_list', to='main.Lesson', verbose_name='lessons'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='mother',
            field=models.CharField(blank=True, max_length=55, null=True, verbose_name='mother'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='own_group',
            field=models.CharField(blank=True, choices=[('UME-I', 'First course'), ('UME-II', 'Second course'), ('UME-III', 'Third course'), ('UME-IV', 'Fourth course')], max_length=7, null=True, verbose_name='own group'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+996999999'. Up to 15 digits allowed", regex='^\\+?996?\\d{9,15}$'), django.core.validators.RegexValidator(message='Please type in the correct format.', regex='^\\+?90\\d{10, 12}$')], verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='status',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='rank'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='teacher_profile', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
