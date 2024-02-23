# Generated by Django 5.0.2 on 2024-02-14 16:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_workers'),
    ]

    operations = [
        migrations.CreateModel(
            name='contract_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work', to='home.works')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worker', to='home.workers')),
            ],
        ),
    ]