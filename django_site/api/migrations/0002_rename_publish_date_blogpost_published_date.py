# Generated by Django 5.1.1 on 2024-10-03 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='publish_date',
            new_name='published_date',
        ),
    ]
