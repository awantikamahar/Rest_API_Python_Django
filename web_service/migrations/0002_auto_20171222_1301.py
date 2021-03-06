# Generated by Django 2.0 on 2017-12-22 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmerCropType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FarmerDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_name', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('taluka', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('pin', models.CharField(max_length=10)),
                ('longitude', models.CharField(max_length=50)),
                ('latitude', models.CharField(max_length=50)),
                ('primary_phone', models.CharField(max_length=15)),
                ('secondary_phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=200)),
                ('land_area', models.CharField(max_length=500)),
                ('soil_color', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FarmerSoilType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soil', models.CharField(max_length=100)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='soil_type', to='web_service.FarmerDetails')),
            ],
        ),
        migrations.AddField(
            model_name='farmercroptype',
            name='farmer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crop_type', to='web_service.FarmerDetails'),
        ),
    ]
