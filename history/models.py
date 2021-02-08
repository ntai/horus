from django.db import models
from meta.models import Location, ValueType

# Create your models here.
class History(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    value_type = models.ForeignKey(ValueType, on_delete=models.CASCADE)
    value = models.FloatField()
    timestamp = models.DateTimeField()
    pass

