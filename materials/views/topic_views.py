from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from ..models import Topic
from ..paginators import TopicListPagination
from ..permissions.topic_permissions import IsAdminANDModeratorCRUDModelTopicPermission
from ..serializers.topic_serializers import TopicSerializer


class TopicCreateAPIView(CreateAPIView):
    """Занесение данных в базу данных о теме."""

    serializer_class = TopicSerializer
    permission_classes = [IsAdminANDModeratorCRUDModelTopicPermission]

    def perform_create(self, serializer):
        """Создание данных в базу данных с текущим пользователем."""

        serializer.save(moderator=self.request.user)


class TopicRetrieveAPIView(RetrieveAPIView):
    """Получение данных о теме."""

    serializer_class = TopicSerializer
    permission_classes = [IsAdminANDModeratorCRUDModelTopicPermission]

    def get_queryset(self):
        """Получение данных с текущим пользователем."""

        return Topic.objects.filter(moderator=self.request.user, pk=self.kwargs['pk'])


class TopicListAPIView(ListAPIView):
    """Получение данных о темах."""

    serializer_class = TopicSerializer
    permission_classes = [IsAdminANDModeratorCRUDModelTopicPermission]
    pagination_class = TopicListPagination

    def get_queryset(self):
        """Получение данных с текущим пользователем."""

        return Topic.objects.filter(moderator=self.request.user)


class TopicUpdateAPIView(UpdateAPIView):
    """Обновление данных о теме."""

    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
    permission_classes = [IsAdminANDModeratorCRUDModelTopicPermission]


class TopicDestroyAPIView(DestroyAPIView):
    """Удаление данных о теме."""

    queryset = Topic.objects.all()
    permission_classes = [IsAdminANDModeratorCRUDModelTopicPermission]
