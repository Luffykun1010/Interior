# Generated by Django 5.0.2 on 2024-02-17 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_works_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='status',
            field=models.CharField(max_length=50),
        ),
    ]
