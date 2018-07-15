from rest_framework import serializers

from .models import Metadata, Tag, Vendor


class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = ('key', 'value')


class TagSerializer(serializers.ModelSerializer):
    metadata = MetadataSerializer(many=True)

    class Meta:
        model = Tag
        fields = ('tag_id', 'metadata')


class VendorSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Vendor
        fields = ('vendor_id', 'tags')
