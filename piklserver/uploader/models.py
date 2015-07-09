from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save

import uuid


class Image(models.Model):
    file = models.FileField()
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=100)


@receiver(pre_save, sender=Image)
def uuid_file_name_callback(sender, instance, *args, **kwargs):
    instance.name = instance.file.name
    instance.file.name = "%s.%s" % (uuid.uuid4(), instance.name.split('.')[-1])
