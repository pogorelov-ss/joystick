# Generated by Django 2.0rc1 on 2017-12-02 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_x', models.IntegerField()),
                ('position_y', models.IntegerField()),
                ('direction_x', models.CharField(max_length=10)),
                ('direction_y', models.CharField(max_length=10)),
                ('direction_angle', models.CharField(max_length=10)),
            ],
        ),
    ]
