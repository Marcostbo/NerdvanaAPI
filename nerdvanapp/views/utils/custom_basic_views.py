from nerdvanapp.constants import PAGINATION_LIMIT, DEFAULT_PAGINATION_LIMIT


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
        limit = int(self.request.query_params.get('limit'))
        offset = int(self.request.query_params.get('offset'))

        headers = {
            'X-Total-Records-Count': queryset.count(),
            'X-Pagination-Default-Limit': PAGINATION_LIMIT,
            'X-Pagination-Maximum-Limit': DEFAULT_PAGINATION_LIMIT,
            'X-Pagination-Limit': limit,
            'X-Pagination-Offset': offset
        }
        paginated_queryset = queryset[offset:offset + limit]

        return paginated_queryset, headers
