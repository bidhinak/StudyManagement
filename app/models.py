from django.db import models


# Create your models here.
class Study(models.Model):
    phases = (
        ('Phase 1', 'Phase 1'),
        ('Phase 2', 'Phase 2'),
        ('Phase 3', 'Phase 3'),
        ('Phase 4', 'Phase 4'),
    )
    study_name = models.CharField(max_length=300)
    study_description = models.TextField()
    study_phase = models.CharField(max_length=100, choices=phases)
    sponsor_name = models.CharField(max_length=100)
