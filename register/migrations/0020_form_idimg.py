# Generated by Django 4.2.7 on 2023-11-17 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0019_remove_form_idimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='idimg',
            field=models.ImageField(max_length=250, null=True, upload_to='media/image/'),
        ),
    ]