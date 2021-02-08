from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)

class LocationLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20
    max_limit = 50
    pass

class LocationPageNumberPagination(PageNumberPagination):
    page_size = 20
    pass

class ValueTypeLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20
    max_limit = 50
    pass

class ValueTypePageNumberPagination(PageNumberPagination):
    page_size = 20
    pass

