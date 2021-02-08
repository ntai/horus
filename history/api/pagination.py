from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)

class HistoryLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20
    max_limit = 50
    pass

class HistoryPageNumberPagination(PageNumberPagination):
    page_size = 20
    pass

