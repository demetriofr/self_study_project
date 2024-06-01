from rest_framework.pagination import PageNumberPagination


class TrainingMatrixListPagination(PageNumberPagination):
    """Пользовательский класс нумерации страниц для списков модели TrainingMatrix."""

    page_size = 5
