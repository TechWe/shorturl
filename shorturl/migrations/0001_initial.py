# Generated by Django 2.0.7 on 2018-07-10 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=20, verbose_name='Short URL')),
                ('click_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Click Time')),
                ('click_ip', models.GenericIPAddressField(default='0.0.0.0', verbose_name='Click IP')),
                ('referrer', models.CharField(default='', max_length=200)),
                ('user_agent', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=20, unique=True, verbose_name='Short URL')),
                ('origin_url', models.URLField(verbose_name='Origin URL')),
                ('title', models.CharField(default='', max_length=100, verbose_name='Title')),
                ('clicks', models.PositiveIntegerField(default=0)),
                ('creator_ip', models.GenericIPAddressField(default='0.0.0.0', verbose_name='IP')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
            ],
        ),
    ]
