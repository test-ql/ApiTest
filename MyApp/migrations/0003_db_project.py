# Generated by Django 4.0.3 on 2022-03-23 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_db_home_href'),
    ]

    operations = [
        migrations.CreateModel(
            name='DB_project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('remark', models.CharField(max_length=1000, null=True)),
                ('user', models.CharField(max_length=15, null=True)),
                ('other_user', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
