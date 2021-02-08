from django.db import models
from common.constant import REST_KEYWORDS
from common.slug import create_name_slug
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class Location(models.Model):
    slug = models.SlugField(max_length=32)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    pass

class ValueType(models.Model):
    slug = models.SlugField(max_length=16)
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name
    pass


# noinspection PyUnusedLocal
@receiver(pre_save, sender=Location)
def pre_save_location_receiver(sender, instance, *args, **kwargs):
    # 100 attendance is the absolute max
    if not instance.slug:
        instance.slug = create_name_slug(sender, instance)
        pass
    pass


# noinspection PyUnusedLocal
@receiver(pre_save, sender=ValueType)
def pre_save_value_type_receiver(sender, instance, *args, **kwargs):
    # 100 attendance is the absolute max
    if not instance.slug:
        instance.slug = create_name_slug(sender, instance)
        pass
    pass
