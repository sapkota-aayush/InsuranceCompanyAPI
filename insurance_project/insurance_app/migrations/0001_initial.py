# Generated by Django 5.1.5 on 2025-03-14 14:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_type', models.CharField(choices=[('LIFE', 'Life Insurance'), ('AUTO', 'Auto Insurance'), ('HOME', 'Home Insurance')], max_length=10)),
                ('premium', models.DecimalField(decimal_places=2, max_digits=10)),
                ('coverage_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='policies', to='insurance_app.customer')),
            ],
        ),
    ]
