# Generated by Django 5.1.7 on 2025-03-23 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0005_remove_asset_associated_risks_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='associated_controls',
        ),
    ]
