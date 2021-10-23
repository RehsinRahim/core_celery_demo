from django.db import models
from django.utils import timezone



class Race(models.Model):
    name = models.CharField(max_length=50, null=False,
                            blank=False, db_index=True)
    status = models.BooleanField(null = True)

    class Meta:
        db_table = "race"




