# Generated by Django 2.2.6 on 2020-07-24 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_detail',
            old_name='P_type',
            new_name='p_type',
        ),
    ]
