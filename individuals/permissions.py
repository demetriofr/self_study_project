from rest_framework.permissions import BasePermission


class IsAdminCRUDAndModeratorCreateModelIndividualPermission(BasePermission):
    """Любой пользователь со статусом администратора может CRUD данные для модели Individual."""

    def has_permission(self, request, view):

        # Проверка статуса пользователя
        return request.user.status_admin or request.user.status_moderator

    def has_object_permission(self, request, view, obj):

        # Дополнительная проверка статуса пользователя на уровне объекта
        return request.user.status_admin or request.user.status_moderator


class IsModeratorReadAndUpdateModelIndividualPermission(BasePermission):
    """Любой пользователь со статусом модератора может редактировать и обновлять данные для модели Individual."""

    def has_object_permission(self, request, view, obj):

        # Дополнительная проверка статуса пользователя на уровне объекта
        return obj.moderator == request.user or obj.is_public_of_moderators
