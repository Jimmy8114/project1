# Generated by Django 2.0.2 on 2019-03-01 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20190301_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oauth_ex',
            name='type',
            field=models.CharField(choices=[('1', 'github'), ('2', 'qq')], max_length=1),
        ),
    ]
