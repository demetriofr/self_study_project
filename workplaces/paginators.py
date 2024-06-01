from rest_framework.pagination import PageNumberPagination


class SOUTCardListPagination(PageNumberPagination):
    """Пользовательский класс нумерации страниц для списков модели SOUTCard."""

    page_size = 5
