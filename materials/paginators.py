from rest_framework.pagination import PageNumberPagination


class AdditionalMaterialListPagination(PageNumberPagination):
    """Пользовательский класс нумерации страниц для списков модели AdditionalMaterial."""

    page_size = 5


class TopicListPagination(PageNumberPagination):
    """Пользовательский класс нумерации страниц для списков модели Topic."""

    page_size = 5


class ModuleListPagination(PageNumberPagination):
    """Пользовательский класс нумерации страниц для списков модели Module."""

    page_size = 5


class ProgramListPagination(PageNumberPagination):
    """Пользовательский класс нумерации страниц для списков модели Program."""

    page_size = 5
