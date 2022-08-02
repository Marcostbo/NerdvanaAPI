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
