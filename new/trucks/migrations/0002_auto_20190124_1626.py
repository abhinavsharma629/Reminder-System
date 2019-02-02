# Generated by Django 2.1.5 on 2019-01-24 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trucksdata',
            name='boolean',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='trucksdata',
            name='insurance_expiry',
            field=models.DateField(default=None),
        ),
    ]