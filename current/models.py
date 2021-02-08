from django.db import models
from meta.models import Location, ValueType

# Create your models here.
class Current(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    value_type = models.ForeignKey(ValueType, on_delete=models.CASCADE)
    value = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.value_type.name + " of " + self.location.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['location', 'value_type'],
                                    name="location's data point")
        ]


