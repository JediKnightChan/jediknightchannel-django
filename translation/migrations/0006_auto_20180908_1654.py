# Generated by Django 2.1.1 on 2018-09-08 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0005_commongamefile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commongamefile',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]