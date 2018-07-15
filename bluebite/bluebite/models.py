from __future__ import unicode_literals

from django.db import models


class Vendor(models.Model):
    vendor_id = models.CharField(primary_key=True, max_length=32)

    def __unicode__(self):
        return '{0}'.format(self.vendor_id)


class Tag(models.Model):
    tag_id = models.CharField(primary_key=True, max_length=32)
    vendor = models.ForeignKey('Vendor', on_delete=models.DO_NOTHING, related_name='tags')

    def __unicode__(self):
        return '{0}'.format(self.tag_id)


class Metadata(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    tags = models.ManyToManyField('Tag', related_name='metadata')

    def __unicode__(self):
        return 'key: {0}, value: {1}'.format(self.key, self.value)
