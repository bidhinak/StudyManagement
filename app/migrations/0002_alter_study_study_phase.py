# Generated by Django 5.1.2 on 2024-11-04 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='study_phase',
            field=models.CharField(choices=[('Phase 1', 'Phase 1'), ('Phase 2', 'Phase 2'), ('Phase 3', 'Phase 3'), ('Phase 4', 'Phase 4')], max_length=100),
        ),
    ]
