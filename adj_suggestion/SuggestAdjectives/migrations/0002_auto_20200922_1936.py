# Generated by Django 3.1.1 on 2020-09-22 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SuggestAdjectives', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Synonyms',
            new_name='Synonym',
        ),
    ]