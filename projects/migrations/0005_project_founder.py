# Generated by Django 5.1.5 on 2025-02-12 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='founder',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
