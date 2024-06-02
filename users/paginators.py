from rest_framework.pagination import PageNumberPagination


class UserListPagination(PageNumberPagination):
    """Пользовательский класс нумерации страниц для списков модели User."""

    page_size = 5


class UserGroupListPagination(PageNumberPagination):
    """Пользовательский класс нумерации страниц для списков модели UserGroup."""

    page_size = 5
