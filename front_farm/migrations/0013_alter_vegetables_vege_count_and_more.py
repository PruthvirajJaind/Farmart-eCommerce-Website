# Generated by Django 4.2.5 on 2023-11-02 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front_farm', '0012_alter_vegetables_selected_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vegetables',
            name='vege_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vegetables',
            name='vege_price',
            field=models.IntegerField(),
        ),
    ]
