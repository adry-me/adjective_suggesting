# Generated by Django 3.1.1 on 2020-09-15 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Synonyms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(max_length=200, verbose_name='original')),
                ('syn', models.TextField(max_length=200, verbose_name='syn')),
            ],
        ),
    ]
