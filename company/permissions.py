from rest_framework.permissions import BasePermission


class IsAdminCRUDModelIndividualPermission(BasePermission):
    """Любой пользователь со статусом администратора может редактировать CRUD модели Individual."""

    def has_permission(self, request, view):

        # Проверка статуса пользователя
        return request.user.status_admin

    def has_object_permission(self, request, view, obj):

        # Дополнительная проверка статуса пользователя на уровне объекта
        return request.user.status_admin


class IsModeratorCRUDModelIndividualPermission(BasePermission):
    """Любой пользователь со статусом модератора может редактировать CRUD модели Individual."""

    def has_permission(self, request, view):

        # Проверка статуса пользователя
        return request.user.status_moderator

    def has_object_permission(self, request, view, obj):

        # Дополнительная проверка статуса пользователя на уровне объекта
        return request.user.status_moderator
