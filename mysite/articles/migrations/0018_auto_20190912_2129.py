# Generated by Django 2.2.5 on 2019-09-12 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0017_auto_20190912_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(related_name='authors', to='articles.Author'),
        ),
    ]