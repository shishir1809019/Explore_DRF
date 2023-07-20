from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class ProductPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'p'
    
class ProductLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 1
    
class ProductCursorPagination(CursorPagination):
    page_size = 1
    ordering = 'price'