# Generated by Django 3.1.5 on 2021-01-10 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0007_auto_20210110_1912'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
