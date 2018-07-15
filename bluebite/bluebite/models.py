from django.db import models


class Vendor(models.Model):
    vendor_id = models.UUIDField(primary_key=True)


class Tag(models.Model):
    tag_id = models.UUIDField(primary_key=True)
    vendor = models.ForeignKey('Vendor', on_delete=models.DO_NOTHING, related_name='tags')
    metadata = models.ManyToManyField('Metadata', related_name='tags')


class Metadata(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
