# Generated by Django 2.0 on 2017-12-29 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_service', '0011_auto_20171229_0611'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_code', models.CharField(max_length=500)),
                ('hsn_sac_code', models.CharField(max_length=200)),
                ('item_name', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=1000)),
                ('uom', models.CharField(max_length=200)),
                ('qty', models.FloatField()),
                ('rate', models.FloatField()),
                ('discount_amount', models.FloatField()),
                ('total_amount', models.FloatField()),
            ],
        ),
    ]