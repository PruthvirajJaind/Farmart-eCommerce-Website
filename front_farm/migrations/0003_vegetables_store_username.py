# Generated by Django 4.2.5 on 2023-10-14 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front_farm', '0002_alter_store_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vegetables',
            name='store_username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='store_veg_name', to='front_farm.store'),
        ),
    ]
