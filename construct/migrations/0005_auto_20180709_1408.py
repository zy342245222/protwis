# Generated by Django 2.0.1 on 2018-07-09 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0004_auto_20180412_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crystallizationtypes',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='crystallizationtypes',
            name='sub_name',
            field=models.CharField(max_length=300, null=True),
        ),
    ]