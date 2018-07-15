from rest_framework import serializers

from .models import Metadata, Tag, Vendor


class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = ('key', 'value')


class TagSerializer(serializers.ModelSerializer):
    metadata = MetadataSerializer(many=True)
    vendor_id = serializers.CharField(required=False)

    class Meta:
        model = Tag
        fields = ('tag_id', 'metadata', 'vendor_id')

    def update(self, instance, validated_data):
        for metadatum in validated_data['metadata']:
            meta, created = Metadata.objects.get_or_create(key=metadatum['key'], value=metadatum['value'])
            if created:
                # brand new Metadata
                meta.tags.add(instance)
            elif not created and instance not in meta.tags.all():
                # add it
                meta.tags.add(instance)
        return instance

    def create(self, validated_data):
        tag = Tag.objects.create(tag_id=validated_data['tag_id'], vendor_id=validated_data['vendor_id'])
        for metadatum in validated_data['metadata']:
            meta, created = Metadata.objects.get_or_create(key=metadatum['key'], value=metadatum['value'])
            if created:
                meta.tags.add(tag)
            elif not created and tag not in meta.tags.all():
                meta.tags.add(tag)
        return tag


class TagDisplaySerializer(serializers.ModelSerializer):
    metadata = MetadataSerializer(many=True)

    class Meta:
        model = Tag
        fields = ('tag_id', 'metadata')


class VendorSerializer(serializers.ModelSerializer):
    tags = TagDisplaySerializer(many=True)

    class Meta:
        model = Vendor
        fields = ('vendor_id', 'tags')

    def create(self, validated_data):
        vendor = Vendor.objects.create(vendor_id=validated_data['vendor_id'])
        for tag in validated_data['tags']:
            new_tag = Tag.objects.create(tag_id=tag['tag_id'], vendor=vendor)
            for metadatum in tag['metadata']:
                meta, created = Metadata.objects.get_or_create(
                    key=metadatum['key'], value=metadatum['value']
                )
                # These will be new tags, so always add them to the metadata
                meta.tags.add(new_tag)
        return vendor
