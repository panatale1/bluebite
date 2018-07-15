import jsonschema
from jsonschema.exceptions import ValidationError
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser

from . import schemas


class JSONSchemaParser(JSONParser):

    def parse(self, stream, media_type=None, parser_context=None):
        data = super(JSONSchemaParser, self).parse(stream, media_type, parser_context)
        try:
            jsonschema.validate(data, schemas.json)
        except ValidationError as error:
            raise ParseError(detail='{0} - {1}[{2}]'.format(
                error.message, error.__dict__['path'][0], error.__dict__['path'][1]))
        else:
            return data
