from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from ..models import AdditionMaterial
from ..paginators import AdditionMaterialListPagination
from ..permissions.addition_material_permissions import IsAdminANDModeratorCRUDModelAdditionMaterialPermission
from ..serializers.addition_material_serializers import AdditionMaterialSerializer


class AdditionMaterialCreateAPIView(CreateAPIView):
    """Занесение данных в базу данных о допматериале."""

    serializer_class = AdditionMaterialSerializer
    permission_classes = [IsAdminANDModeratorCRUDModelAdditionMaterialPermission]

    def perform_create(self, serializer):
        """Создание данных в базу данных с текущим пользователем."""

        serializer.save(moderator=self.request.user)


class AdditionMaterialRetrieveAPIView(RetrieveAPIView):
    """Получение данных о допматериале."""

    serializer_class = AdditionMaterialSerializer
    permission_classes = [IsAdminANDModeratorCRUDModelAdditionMaterialPermission]

    def get_queryset(self):
        """Получение данных с текущим пользователем."""

        return AdditionMaterial.objects.filter(moderator=self.request.user, pk=self.kwargs['pk'])


class AdditionMaterialListAPIView(ListAPIView):
    """Получение данных о допматериалах."""

    serializer_class = AdditionMaterialSerializer
    permission_classes = [IsAdminANDModeratorCRUDModelAdditionMaterialPermission]
    pagination_class = AdditionMaterialListPagination

    def get_queryset(self):
        """Получение данных с текущим пользователем."""

        return AdditionMaterial.objects.filter(moderator=self.request.user)


class AdditionMaterialUpdateAPIView(UpdateAPIView):
    """Обновление данных о допматериале."""

    serializer_class = AdditionMaterialSerializer
    queryset = AdditionMaterial.objects.all()
    permission_classes = [IsAdminANDModeratorCRUDModelAdditionMaterialPermission]


class AdditionMaterialDestroyAPIView(DestroyAPIView):
    """Удаление данных о допматериале."""

    queryset = AdditionMaterial.objects.all()
    permission_classes = [IsAdminANDModeratorCRUDModelAdditionMaterialPermission]
