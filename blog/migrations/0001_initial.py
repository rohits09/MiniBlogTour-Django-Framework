# Generated by Django 3.1.4 on 2021-04-09 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=18)),
                ('title', models.CharField(max_length=150)),
                ('descpt', models.TextField(max_length=1818)),
            ],
        ),
    ]
