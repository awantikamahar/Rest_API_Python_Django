# Generated by Django 2.0 on 2017-12-23 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_service', '0003_cultivationform'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('sample_request', models.CharField(max_length=200)),
                ('sample_request_qauntity', models.IntegerField()),
                ('sample_given_date', models.DateTimeField(auto_now_add=True)),
                ('photo_upload', models.CharField(max_length=1000)),
                ('excepted_result_date', models.DateTimeField(null=True)),
                ('excepted_result_photo', models.CharField(max_length=1000, null=True)),
                ('excepted_result_note', models.CharField(max_length=500, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('farmer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='farmer_sample', to='web_service.FarmerDetails')),
            ],
        ),
        migrations.AlterField(
            model_name='cultivationform',
            name='farmer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='farmer', to='web_service.FarmerDetails'),
        ),
        migrations.AlterField(
            model_name='cultivationform',
            name='soil_test_report',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cultivationform',
            name='water_test_report',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
