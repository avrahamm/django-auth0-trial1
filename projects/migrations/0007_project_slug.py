# Generated by Django 5.1.5 on 2025-02-20 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
