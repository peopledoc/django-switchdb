# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ItemForTest(models.Model):
    name = models.CharField("Name", max_length=120)

    def __unicode__(self):
        return self.name
