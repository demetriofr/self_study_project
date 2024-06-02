from rest_framework.pagination import PageNumberPagination


class OrganizationListPagination(PageNumberPagination):
    """Пользовательский класс нумерации страниц для списков модели Organization."""

    page_size = 5


class DepartmentListPagination(PageNumberPagination):
    """Пользовательский класс нумерации страниц для списков модели Department."""

    page_size = 5


class PositionListPagination(PageNumberPagination):
    """Пользовательский класс нумерации страниц для списков модели Position."""

    page_size = 5


class WorkerListPagination(PageNumberPagination):
    """Пользовательский класс нумерации страниц для списков модели Worker."""

    page_size = 5
