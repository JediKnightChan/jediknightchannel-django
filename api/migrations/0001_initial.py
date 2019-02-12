# Generated by Django 2.1.1 on 2018-09-14 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ip', models.GenericIPAddressField()),
                ('social_network', models.CharField(choices=[('vk', 'VKontacte'), ('google', 'Google'), ('yandex', 'Yandex')], max_length=20)),
                ('stage', models.CharField(choices=[(1, 'request_created'), (2, 'login_started'), (3, 'login_completed')], max_length=30)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]