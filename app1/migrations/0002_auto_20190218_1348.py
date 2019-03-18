# Generated by Django 2.0.2 on 2019-02-18 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_id', models.IntegerField()),
                ('manager_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_id', models.IntegerField()),
                ('school_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='manager',
            name='my_school',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.School'),
        ),
    ]