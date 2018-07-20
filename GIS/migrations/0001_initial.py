# Generated by Django 2.0.7 on 2018-07-20 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=120)),
                ('date_created', models.DateTimeField()),
                ('last_modified', models.DateTimeField()),
                ('governate', models.CharField(max_length=120)),
                ('area', models.CharField(max_length=120)),
                ('block', models.CharField(max_length=120)),
                ('street', models.CharField(max_length=120)),
                ('house', models.CharField(max_length=120)),
                ('paci_serial', models.CharField(max_length=120)),
                ('land_size', models.CharField(max_length=120)),
            ],
        ),
    ]
