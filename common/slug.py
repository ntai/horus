from django.utils.text import slugify
from django.db import models
from .constant import REST_KEYWORDS

def create_name_slug(class_obj: models.Model, instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
        pass

    # If the slug is REST verbs, avoid the conflict.
    exists = slug in REST_KEYWORDS or slug in ['location', 'locations' ]
    qs = None
    if not exists:
        qs = class_obj.objects.filter(slug=slug).order_by("-id")
        exists = qs.exists()
        pass
    if exists and qs:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_name_slug(class_obj.objects, instance, new_slug=new_slug)
    return slug
