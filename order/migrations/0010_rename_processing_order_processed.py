# Generated by Django 4.0.5 on 2022-07-21 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_rename_status_order_processing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='processing',
            new_name='processed',
        ),
    ]