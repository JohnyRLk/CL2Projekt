# Generated by Django 2.2.1 on 2019-05-22 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('excercise', '0005_auto_20190517_0837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turnament',
            name='grade',
        ),
    ]
