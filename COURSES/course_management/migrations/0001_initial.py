# Generated by Django 4.2.7 on 2024-01-14 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortTermCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(default=None, upload_to='')),
                ('amount', models.FloatField()),
                ('additional_information', models.TextField()),
                ('status', models.CharField(choices=[('Enable', 'Enable'), ('Disable', 'Disable')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('Email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
