# Generated by Django 4.2.5 on 2023-09-18 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, verbose_name='User Email')),
                ('phone', models.CharField(max_length=15, verbose_name='Contact Phone')),
                ('zip_code', models.CharField(max_length=30, verbose_name='Zip Code')),
                ('address', models.CharField(max_length=300)),
                ('web', models.URLField(blank=True, verbose_name='Website Address')),
            ],
        ),
    ]
