# Generated by Django 2.1.5 on 2019-01-24 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0004_remove_notifications_boolean1'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='fitness_id',
            field=models.CharField(default=-1, max_length=30),
        ),
        migrations.AddField(
            model_name='notifications',
            name='insurance_id',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='truck_number',
            field=models.CharField(max_length=14),
        ),
    ]
