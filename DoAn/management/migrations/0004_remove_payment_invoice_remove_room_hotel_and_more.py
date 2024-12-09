# Generated by Django 5.0.10 on 2024-12-09 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_alter_hotel_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='invoice',
        ),
        migrations.RemoveField(
            model_name='room',
            name='hotel',
        ),
        migrations.DeleteModel(
            name='Invoice',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
    ]