# Generated by Django 2.1.1 on 2018-09-08 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0004_gameclass_fraction'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonGameFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content_file', models.FileField(upload_to='translation/common/')),
            ],
        ),
    ]
