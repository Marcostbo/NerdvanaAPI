from nerdvanapp.constants import PAGINATION_LIMIT, DEFAULT_PAGINATION_LIMIT
from rest_framework.exceptions import ValidationError


class SerializerFilterView:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.request = None
        self.serializers = None
        self.default_serializer = None

    def get_serializer_class(self):
        selected_serializer = self.request.query_params.get('serializer')
        if selected_serializer:
            for serializer in self.serializers:
                if serializer.Meta.api_filter_name == selected_serializer:
                    return serializer
        return self.default_serializer


class PaginatedViewSet:
    def __init__(self):
        self.request = None

    def paginate_queryset(self, queryset):

        limit, offset = self.validate_limit_offset_input()

        headers = {
            'X-Total-Records-Count': queryset.count(),
            'X-Pagination-Default-Limit': PAGINATION_LIMIT,
            'X-Pagination-Maximum-Limit': DEFAULT_PAGINATION_LIMIT,
            'X-Pagination-Limit': limit,
            'X-Pagination-Offset': offset
        }
        paginated_queryset = queryset[offset:offset + limit]

        return paginated_queryset, headers

    def validate_limit_offset_input(self):

        limit = self.request.query_params.get('limit')
        offset = self.request.query_params.get('offset')

        if not self.request.query_params.get('offset'):
            raise ValidationError('Select an offset')
        if not limit:
            limit = DEFAULT_PAGINATION_LIMIT
        elif int(limit) > PAGINATION_LIMIT:
            limit = DEFAULT_PAGINATION_LIMIT

        return int(limit), int(offset)
