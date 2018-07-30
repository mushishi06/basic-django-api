# Generated by Django 2.0.7 on 2018-07-29 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20180729_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='code',
            field=models.CharField(default='', max_length=5, unique=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.DeleteModel(
            name='Code',
        ),
    ]