# Generated by Django 3.2.9 on 2021-11-21 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pins', '0002_alter_pin_topics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pin',
            name='saved_by',
        ),
    ]
