# Generated by Django 2.2.5 on 2019-09-11 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_auto_20190911_2336'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]