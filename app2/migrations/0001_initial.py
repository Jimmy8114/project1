# Generated by Django 2.0.2 on 2019-03-06 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computerName', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('discription', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Iphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iphoneName', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('discription', models.CharField(max_length=100)),
            ],
        ),
    ]