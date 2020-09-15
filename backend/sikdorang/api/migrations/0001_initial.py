# Generated by Django 2.2.7 on 2020-09-14 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('store_name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=20, null=True)),
                ('tel', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('latitude', models.FloatField(max_length=10, null=True)),
                ('longitude', models.FloatField(max_length=10, null=True)),
                ('category', models.ManyToManyField(related_name='store_category', to='api.Category')),
                ('tags', models.ManyToManyField(related_name='store_tags', to='api.Tags')),
            ],
        ),
    ]
