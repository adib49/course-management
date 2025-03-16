# Generated by Django 5.0.10 on 2025-03-16 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0007_alter_customuser_unique_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='unique_code',
            field=models.CharField(blank=True, max_length=5, null=True, unique=True),
        ),
    ]
