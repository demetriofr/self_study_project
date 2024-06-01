from rest_framework.pagination import PageNumberPagination


class QuestionListPagination(PageNumberPagination):
    """Пользовательский класс нумерации страниц для списков модели Question."""

    page_size = 5


class TestListPagination(PageNumberPagination):
    """Пользовательский класс нумерации страниц для списков модели Test."""

    page_size = 5


class TestingListPagination(PageNumberPagination):
    """Пользовательский класс нумерации страниц для списков модели Testing."""

    page_size = 5
