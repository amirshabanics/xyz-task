# Generated by Django 4.1.3 on 2022-12-03 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0002_alter_index_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]