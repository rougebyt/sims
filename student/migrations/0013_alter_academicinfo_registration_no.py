# Generated by Django 5.1.5 on 2025-01-31 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_auto_20200419_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinfo',
            name='registration_no',
            field=models.IntegerField(default=249793, unique=True),
        ),
    ]
