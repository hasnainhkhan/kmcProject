# Generated by Django 4.2.5 on 2023-10-28 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_alter_form_idimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='idimg',
            field=models.FileField(null=True, upload_to='image/'),
        ),
    ]