from django.db import models
from django.utils import timezone

class BaseTimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True

# Create your models here.
class Farmer(BaseTimestampedModel):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=
        (
            ('m', "Male",),
            ('f', "Female",),
        ),
        null=True,
    )

    def __str__(self):
        return self.name

class Farm(BaseTimestampedModel):
    owner = models.ForeignKey(Farmer, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    area = models.DecimalField(decimal_places=2, max_digits=6, default=0)

    def __str__(self):
        return self.name

