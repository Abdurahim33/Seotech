# Generated by Django 5.0.3 on 2024-03-10 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='work_department',
            options={'verbose_name': 'Work_department', 'verbose_name_plural': 'Work_departments'},
        ),
    ]