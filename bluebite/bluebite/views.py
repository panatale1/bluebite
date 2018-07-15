from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from .filters import VendorFilter
from .models import Vendor, Tag
from .serializers import VendorSerializer, TagSerializer


class VendorListView(ListAPIView):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = VendorFilter


class TagListView(ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('tag_id', 'metadata__key', 'metadata__value')
