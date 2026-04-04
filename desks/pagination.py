from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination


class StandartPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'limit'
    page_query_param = 'page'
    max_page_size = 6


