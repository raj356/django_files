# Generated by Django 3.1.4 on 2020-12-18 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=1)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='\\media')),
                ('sub', models.CharField(max_length=3, null=True)),
            ],
        ),
    ]
