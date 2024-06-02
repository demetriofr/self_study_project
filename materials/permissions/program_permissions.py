from rest_framework.permissions import BasePermission


class IsAdminModeratorAndStudentReadModelProgramPermission(BasePermission):
    """Любой пользователь со статусом администратора может просматривать модели Program."""

    def has_permission(self, request, view):

        # Проверка статуса пользователя
        return request.user.status_admin or request.user.status_moderator or request.user.status_student

    def has_object_permission(self, request, view, obj):

        # Дополнительная проверка статуса пользователя на уровне объекта
        return request.user.status_admin or request.user.status_moderator or request.user.status_student


class IsAdminANDModeratorCRUDModelProgramPermission(BasePermission):
    """Любой пользователь со статусом администратора может редактировать CRUD модели Program."""

    def has_permission(self, request, view):

        # Проверка статуса пользователя
        return request.user.status_admin or request.user.status_moderator

    def has_object_permission(self, request, view, obj):

        # Дополнительная проверка статуса пользователя на уровне объекта
        return request.user.status_admin or request.user.status_moderator
