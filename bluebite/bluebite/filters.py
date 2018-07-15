from django_filters import rest_framework as filters

from .models import Vendor


class VendorFilter(filters.FilterSet):
    tag_id = filters.CharFilter(name='tags__tag_id', lookup_expr='iexact')
    metadata_key = filters.CharFilter(name='tags__metadata__key', lookup_expr='iexact')
    metadata_value = filters.CharFilter(name='tags__metadata__value', lookup_expr='iexact')

    class Meta:
        model = Vendor
        fields = ['vendor_id', 'tags']
