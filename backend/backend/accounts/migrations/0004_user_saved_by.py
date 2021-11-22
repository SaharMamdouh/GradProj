# Generated by Django 3.2.9 on 2021-11-21 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pins', '0003_remove_pin_saved_by'),
        ('accounts', '0003_alter_user_interest'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='saved_by',
            field=models.ManyToManyField(related_name='saved_pins', through='pins.Save', to='pins.Pin'),
        ),
    ]
