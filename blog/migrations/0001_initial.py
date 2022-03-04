# Generated by Django 4.0.1 on 2022-02-11 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.CharField(max_length=250)),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
