from rest_framework.permissions import BasePermission


class IsAdminCRUDModelSOUTCardPermission(BasePermission):
    """Любой пользователь со статусом администратора может редактировать CRUD модели SOUTCard."""

    def has_permission(self, request, view):

        # Проверка статуса пользователя
        return request.user.status_admin

    def has_object_permission(self, request, view, obj):

        # Дополнительная проверка статуса пользователя на уровне объекта
        return request.user.status_admin

