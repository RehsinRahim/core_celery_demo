from django.db import models
from django.utils import timezone



class Race(models.Model):
    name = models.CharField(max_length=50, null=False,
                            blank=False, db_index=True)
    status = models.BooleanField(null = True)

    class Meta:
        db_table = "race"


    # def save(self, *args, **kwargs):
    #     create_task = False 
    #     if self.pk is None: 
    #         create_task = True 

    #     super(Race, self).save(*args, **kwargs) 

    #     if create_task: 
    #         set_race_as_inactive.apply_async(args=[self], eta=self.end_time) 


