# Generated by Django 2.2 on 2019-11-17 01:16

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('description', models.TextField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryInCountry',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('id_country', models.TextField(db_index=True, help_text='Country reference')),
                ('id_category', models.TextField(help_text='Category reference')),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('id_category_in_country', models.TextField()),
                ('name', models.TextField(default=None, null=True)),
                ('description', models.TextField(default=None, null=True)),
                ('price', models.FloatField(default=None, null=True)),
                ('link', models.TextField(default='https://google.com')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('home_country', models.TextField(help_text='Country reference')),
                ('interests', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), help_text='List of Category references', size=None)),
                ('countries', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), help_text='List of Country references. Length of this field MUST be equal to length of "results"', size=None)),
                ('results', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, help_text='List of JSON. Length of this field MUST be equal to length of "countries"', size=None)),
                ('prepared', models.BooleanField(default=False)),
            ],
        ),
    ]
