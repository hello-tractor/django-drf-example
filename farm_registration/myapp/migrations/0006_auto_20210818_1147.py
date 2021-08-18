# Generated by Django 3.2.6 on 2021-08-18 11:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_farm_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='farm',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farm',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='farmer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farmer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
