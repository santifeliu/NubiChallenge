# Generated by Django 4.1 on 2023-10-25 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nubi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='uuid',
            new_name='wallet_id',
        ),
    ]
