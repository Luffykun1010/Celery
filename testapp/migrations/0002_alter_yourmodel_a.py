# Generated by Django 5.0.2 on 2024-02-21 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yourmodel',
            name='a',
            field=models.CharField(max_length=10),
        ),
    ]
