# Generated by Django 4.2.5 on 2023-10-31 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0011_remove_complain_complain_complain_scomplain'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplainRaised',
            fields=[
                ('sn', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=5)),
                ('email', models.CharField(max_length=15)),
                ('contact', models.CharField(max_length=15)),
                ('compln', models.TextField(max_length=255, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='CompLain',
        ),
    ]