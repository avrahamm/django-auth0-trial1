# Generated by Django 5.1.5 on 2025-02-12 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_founder'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
