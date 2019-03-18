# Generated by Django 2.0.2 on 2019-02-18 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20190218_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('student_name', models.CharField(max_length=20)),
                ('my_school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.School')),
            ],
        ),
    ]