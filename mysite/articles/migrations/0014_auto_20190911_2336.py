# Generated by Django 2.2.5 on 2019-09-11 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_auto_20190911_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='comments',
        ),
        migrations.AddField(
            model_name='comments',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Article'),
        ),
    ]
