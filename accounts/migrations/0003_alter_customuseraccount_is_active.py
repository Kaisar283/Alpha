# Generated by Django 4.0.6 on 2022-07-08 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuseraccount_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuseraccount',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
