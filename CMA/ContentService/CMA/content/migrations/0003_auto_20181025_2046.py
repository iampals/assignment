# Generated by Django 2.1.2 on 2018-10-25 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20181025_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='pagename',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]