from rest_framework.pagination import PageNumberPagination


class AdPagination(PageNumberPagination):
    """
    Пагинатор вывода объявлений
    """
    page_size = 5
