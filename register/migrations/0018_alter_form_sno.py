# Generated by Django 4.2.5 on 2023-11-06 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0017_alter_form_sno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='sno',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]