from django.db import models


class Pic(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    pic_name = models.CharField(max_length=50, blank=True, null=True)


class Trunk(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)
    engine = models.CharField(max_length=50, blank=True, null=True)
    gear_box = models.CharField(max_length=50, blank=True, null=True)
    carr_length = models.CharField(max_length=50, blank=True, null=True)
    tf_drive = models.CharField(max_length=50, blank=True, null=True)
    carr_st = models.CharField(max_length=50, blank=True, null=True)
    emiss_standard = models.CharField(max_length=50, blank=True, null=True)

