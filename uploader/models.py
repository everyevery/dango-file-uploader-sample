from django.db import models

# from django.piklserver.settings import MEDIA_ROOT

import uuid
import os


class Image(models.Model):
    file = models.FileField()
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=100)
