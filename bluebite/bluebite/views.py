from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ParseError, ValidationError
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .filters import VendorFilter
from .models import Vendor, Tag
from .parsers import JSONSchemaParser
from .serializers import VendorSerializer, TagSerializer, TagDisplaySerializer


class VendorListView(APIView):
    filter_backends = (DjangoFilterBackend,)
    filter_class = VendorFilter
    parser_classes = (JSONSchemaParser,)

    def get(self, request, _format=None):
        serializer = VendorSerializer(Vendor.objects.all(), many=True)
        return Response(serializer.data)

    def get_vendor(self, request):
        return Vendor.objects.get(vendor_id=request.data['vendor_id'])

    def get_tag(self, tag_id):
        return Tag.objects.get(tag_id=tag_id)

    def post(self, request, _format=None):
        errors = []
        try:
            request.data
        except (ParseError, ValidationError) as error:
            return Response(
                'Invalid JSON - {0}'.format(error.detail), status=status.HTTP_400_BAD_REQUEST
            )
        if Vendor.objects.filter(vendor_id=request.data['vendor_id']).exists():
            serializer = VendorSerializer(self.get_vendor(request), request.data)
        else:
            serializer = VendorSerializer(data=request.data)
        if not serializer.is_valid():
            tags = request.data['tags']
            for tag in tags:
                tag.update({'vendor_id': request.data['vendor_id']})
                if Tag.objects.filter(tag_id=tag['tag_id']).exists():
                    serializer = TagSerializer(self.get_tag(tag['tag_id']), tag)
                else:
                    serializer = TagSerializer(data=tag)
                if serializer.is_valid():
                    serializer.save()
                else:
                    errors.append(serializer.errors)
        if not errors:
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)



class TagListView(ListAPIView):
    serializer_class = TagDisplaySerializer
    queryset = Tag.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('tag_id', 'metadata__key', 'metadata__value')
