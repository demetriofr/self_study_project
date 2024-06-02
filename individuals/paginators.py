from rest_framework.pagination import PageNumberPagination


class IndividualListPagination(PageNumberPagination):
    """Пользовательский класс нумерации страниц для списков модели Individual."""

    page_size = 5
