# Generated by Django 3.1.5 on 2022-04-13 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='done',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
