# Generated by Django 2.2.5 on 2021-04-17 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(blank=True, max_length=150, null=True)),
                ('subject_teach', models.CharField(blank=True, max_length=150, null=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('area', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(blank=True, max_length=150, null=True)),
                ('salary_per_month', models.CharField(blank=True, max_length=150, null=True)),
                ('preffered_area', models.CharField(blank=True, max_length=150, null=True)),
                ('online_teach_exp', models.FloatField(blank=True, max_length=100, null=True)),
                ('total_teach_exp', models.FloatField(blank=True, max_length=100, null=True)),
                ('qualification', models.CharField(blank=True, max_length=250, null=True)),
                ('tutor_type', models.CharField(blank=True, choices=[('Inhouse', 'Inhouse'), ('Online', 'Online'), ('Inhouse & Online', 'Inhouse & Online')], default='Inhouse', max_length=25, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('bio', models.CharField(blank=True, max_length=450, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to=home.models.path_and_rename, verbose_name='profile picture')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(blank=True, max_length=150, null=True)),
                ('department', models.CharField(blank=True, max_length=150, null=True)),
                ('class_level', models.CharField(blank=True, max_length=150, null=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('area', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(blank=True, max_length=150, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], default='male', max_length=15, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('bio', models.CharField(blank=True, max_length=450, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to=home.models.path_and_rename, verbose_name='profile picture')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
