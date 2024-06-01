from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from .models import SOUTCard
from .serializers import SOUTCardSerializer


class SOUTCardCreateAPIView(CreateAPIView):
    """Занесение данных в базу данных о карточке СОУТ."""

    serializer_class = SOUTCardSerializer

    def perform_create(self, serializer):
        """Создание данных в базу данных с текущим пользователем."""

        serializer.save(admin=self.request.user)


class SOUTCardRetrieveAPIView(RetrieveAPIView):
    """Получение данных о карточке СОУТ."""

    serializer_class = SOUTCardSerializer

    def get_object(self):
        """Получение данных с текущим пользователем."""

        return SOUTCard.objects.get(admin=self.request.user)


class SOUTCardListAPIView(ListAPIView):
    """Получение данных о карточках СОУТ."""

    serializer_class = SOUTCardSerializer

    def get_queryset(self):
        """Получение данных с текущим пользователем."""

        return SOUTCard.objects.filter(admin=self.request.user)


class SOUTCardUpdateAPIView(UpdateAPIView):
    """Обновление данных о карточке СОУТ."""

    serializer_class = SOUTCardSerializer
    queryset = SOUTCard.objects.all()


class SOUTCardDestroyAPIView(DestroyAPIView):
    """Удаление данных о карточке СОУТ."""

    queryset = SOUTCard.objects.all()
