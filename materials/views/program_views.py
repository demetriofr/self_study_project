from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from ..models import Program
from ..paginators import ProgramListPagination
from ..permissions.program_permissions import (
    IsAdminANDModeratorCRUDModelProgramPermission,
    IsAdminModeratorAndStudentReadModelProgramPermission
)
from ..serializers.program_serializers import ProgramSerializer


class ProgramCreateAPIView(CreateAPIView):
    """Занесение данных в базу данных о модуле."""

    serializer_class = ProgramSerializer
    permission_classes = [IsAdminANDModeratorCRUDModelProgramPermission]

    def perform_create(self, serializer):
        """Создание данных в базу данных с текущим пользователем."""

        serializer.save(moderator=self.request.user)


class ProgramRetrieveAPIView(RetrieveAPIView):
    """Получение данных о модуле."""

    serializer_class = ProgramSerializer
    permission_classes = [IsAdminANDModeratorCRUDModelProgramPermission]

    def get_queryset(self):
        """Получение данных с текущим пользователем."""

        return Program.objects.filter(pk=self.kwargs['pk'],
                                      moderator=self.request.user
                                      )


class ProgramRetrieveAllAPIView(RetrieveAPIView):
    """Получение данных о модуле."""

    serializer_class = ProgramSerializer
    permission_classes = [IsAdminModeratorAndStudentReadModelProgramPermission]

    def get_queryset(self):
        """Получение данных с текущим пользователем."""

        return Program.objects.filter(is_public=True, pk=self.kwargs['pk'])


class ProgramListAPIView(ListAPIView):
    """Получение данных о модулях."""

    serializer_class = ProgramSerializer
    permission_classes = [IsAdminANDModeratorCRUDModelProgramPermission]
    pagination_class = ProgramListPagination

    def get_queryset(self):
        """Получение данных с текущим пользователем."""

        return Program.objects.filter(moderator=self.request.user)


class ProgramUpdateAPIView(UpdateAPIView):
    """Обновление данных о модуле."""

    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
    permission_classes = [IsAdminANDModeratorCRUDModelProgramPermission]


class ProgramDestroyAPIView(DestroyAPIView):
    """Удаление данных о модуле."""

    queryset = Program.objects.all()
    permission_classes = [IsAdminANDModeratorCRUDModelProgramPermission]
