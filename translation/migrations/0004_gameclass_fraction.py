# Generated by Django 2.1.1 on 2018-09-07 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0003_auto_20180907_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameclass',
            name='fraction',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]