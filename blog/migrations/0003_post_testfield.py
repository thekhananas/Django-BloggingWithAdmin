# Generated by Django 3.0.13 on 2021-03-15 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210315_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='testField',
            field=models.CharField(default='AnasKhanTesting', max_length=250),
        ),
    ]
