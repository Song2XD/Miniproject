# Generated by Django 5.1.5 on 2025-02-26 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S_id', models.CharField(max_length=10, unique=True)),
                ('Brand', models.CharField(max_length=100, unique=True)),
                ('Name', models.CharField(max_length=100)),
                ('descrip', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(default=0)),
            ],
        ),
    ]
