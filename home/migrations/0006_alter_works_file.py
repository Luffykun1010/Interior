# Generated by Django 5.0.2 on 2024-02-17 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_works_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='file',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]