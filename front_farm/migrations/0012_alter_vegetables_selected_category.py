# Generated by Django 4.2.5 on 2023-11-01 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front_farm', '0011_alter_vegetables_selected_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vegetables',
            name='selected_category',
            field=models.CharField(blank=True, choices=[('vegetables', 'Vegetables'), ('fruits', 'Fruits'), ('flowers', 'Flowers'), ('home_products', 'Home Products')], max_length=20, null=True),
        ),
    ]
