# Generated by Django 4.2.6 on 2023-11-18 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_disabled_info_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disabled_info',
            name='sex',
            field=models.CharField(choices=[('1', 'Kobieta'), ('2', 'Mężczyzna')], default='green', max_length=10),
        ),
    ]
