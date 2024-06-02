from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from .models import Individual
from .paginators import IndividualListPagination
from .permissions import (
    IsAdminCRUDAndModeratorCreateModelIndividualPermission,
    IsModeratorReadAndUpdateModelIndividualPermission
)
from .serializers import IndividualSerializer


class IndividualCreateAPIView(CreateAPIView):
    """Занесение данных в базу данных о физлице."""

    serializer_class = IndividualSerializer
    permission_classes = [
        IsAdminCRUDAndModeratorCreateModelIndividualPermission
    ]

    def perform_create(self, serializer):
        """Создание данных в базу данных с текущим пользователем."""

        serializer.save(moderator=self.request.user)


class IndividualRetrieveAPIView(RetrieveAPIView):
    """Получение данных о физлице."""

    serializer_class = IndividualSerializer
    permission_classes = [
        IsAdminCRUDAndModeratorCreateModelIndividualPermission,
        IsModeratorReadAndUpdateModelIndividualPermission
    ]

    def get_queryset(self):
        """Получение данных с текущим пользователем."""

        return Individual.objects.filter(moderator=self.request.user, pk=self.kwargs['pk'])


class IndividualListAPIView(ListAPIView):
    """Получение данных о физлицах."""

    serializer_class = IndividualSerializer
    permission_classes = [
        IsAdminCRUDAndModeratorCreateModelIndividualPermission,
        IsModeratorReadAndUpdateModelIndividualPermission
    ]
    pagination_class = IndividualListPagination

    def get_queryset(self):
        """Получение данных с текущим пользователем."""

        return Individual.objects.filter(moderator=self.request.user)


class IndividualUpdateAPIView(UpdateAPIView):
    """Обновление данных о физлице."""

    serializer_class = IndividualSerializer
    queryset = Individual.objects.all()
    permission_classes = [
        IsAdminCRUDAndModeratorCreateModelIndividualPermission,
        IsModeratorReadAndUpdateModelIndividualPermission
    ]


class IndividualDestroyAPIView(DestroyAPIView):
    """Удаление данных о физлице."""

    queryset = Individual.objects.all()
    permission_classes = [IsAdminCRUDAndModeratorCreateModelIndividualPermission]
