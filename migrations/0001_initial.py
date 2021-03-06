# Generated by Django 3.0.8 on 2020-07-25 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pregnant_details',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_fname', models.CharField(max_length=200)),
                ('p_lname', models.CharField(max_length=200)),
                ('p_dob', models.DateField()),
                ('p_email_id', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('p_phone_number', models.CharField(max_length=10, unique=True)),
                ('p_adhar_number', models.BigIntegerField()),
                ('p_address', models.CharField(max_length=500)),
                ('p_pincode', models.IntegerField(max_length=6)),
                ('state', models.CharField(default='Null', max_length=50)),
                ('city', models.CharField(default='Null', max_length=50)),
                ('p_reg_date', models.DateTimeField(auto_now=True)),
                ('p_how_many_months_pregnant', models.IntegerField(max_length=200, null=True)),
                ('p_expected_delivery_date', models.DateField()),
            ],
            options={
                'db_table': 'pregnant_details',
            },
        ),
    ]
