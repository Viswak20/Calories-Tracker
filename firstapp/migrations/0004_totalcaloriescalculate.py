# Generated by Django 5.0.4 on 2024-04-29 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_totalcalories'),
    ]

    operations = [
        migrations.CreateModel(
            name='totalcaloriescalculate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
            ],
        ),
    ]
