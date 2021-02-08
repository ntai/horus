from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)

class CurrentLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20
    max_limit = 50
    pass

class CurrentPageNumberPagination(PageNumberPagination):
    page_size = 20
    pass

