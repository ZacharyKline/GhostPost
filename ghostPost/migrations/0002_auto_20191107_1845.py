# Generated by Django 2.2.7 on 2019-11-07 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostPost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boastnroast',
            name='boast',
            field=models.BooleanField(default=False),
        ),
    ]
