# Generated by Django 5.0.4 on 2024-04-24 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_dinner_dinnercarbohydrate_dinner_dinnerfat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='totalcalories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eatenfoods', models.CharField(max_length=25)),
                ('totalcalories', models.IntegerField()),
                ('totalprotein', models.IntegerField()),
                ('totalcarbohydrate', models.IntegerField()),
                ('totalfat', models.IntegerField()),
            ],
        ),
    ]
