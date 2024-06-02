from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from ..models import Module
from ..paginators import ModuleListPagination
from ..permissions.module_permissions import IsAdminANDModeratorCRUDModelModulePermission
from ..serializers.module_serializers import ModuleSerializer


class ModuleCreateAPIView(CreateAPIView):
    """Занесение данных в базу данных о модуле."""

    serializer_class = ModuleSerializer
    permission_classes = [IsAdminANDModeratorCRUDModelModulePermission]

    def perform_create(self, serializer):
        """Создание данных в базу данных с текущим пользователем."""

        serializer.save(moderator=self.request.user)


class ModuleRetrieveAPIView(RetrieveAPIView):
    """Получение данных о модуле."""

    serializer_class = ModuleSerializer
    permission_classes = [IsAdminANDModeratorCRUDModelModulePermission]

    def get_queryset(self):
        """Получение данных с текущим пользователем."""

        return Module.objects.filter(moderator=self.request.user, pk=self.kwargs['pk'])


class ModuleListAPIView(ListAPIView):
    """Получение данных о модулях."""

    serializer_class = ModuleSerializer
    permission_classes = [IsAdminANDModeratorCRUDModelModulePermission]
    pagination_class = ModuleListPagination

    def get_queryset(self):
        """Получение данных с текущим пользователем."""

        return Module.objects.filter(moderator=self.request.user)


class ModuleUpdateAPIView(UpdateAPIView):
    """Обновление данных о модуле."""

    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsAdminANDModeratorCRUDModelModulePermission]


class ModuleDestroyAPIView(DestroyAPIView):
    """Удаление данных о модуле."""

    queryset = Module.objects.all()
    permission_classes = [IsAdminANDModeratorCRUDModelModulePermission]
