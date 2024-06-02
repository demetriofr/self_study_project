from django.urls import path

from .apps import MaterialsConfig
from .views.addition_material_views import (
    AdditionMaterialCreateAPIView,
    AdditionMaterialRetrieveAPIView,
    AdditionMaterialListAPIView,
    AdditionMaterialUpdateAPIView,
    AdditionMaterialDestroyAPIView,
)
from .views.topic_views import (
    TopicCreateAPIView,
    TopicRetrieveAPIView,
    TopicListAPIView,
    TopicUpdateAPIView,
    TopicDestroyAPIView
)
from .views.module_views import (
    ModuleCreateAPIView,
    ModuleRetrieveAPIView,
    ModuleListAPIView,
    ModuleUpdateAPIView,
    ModuleDestroyAPIView
)
from .views.program_views import (
    ProgramCreateAPIView,
    ProgramRetrieveAPIView,
    ProgramRetrieveAllAPIView,
    ProgramListAPIView,
    ProgramUpdateAPIView,
    ProgramDestroyAPIView
)


app_name = MaterialsConfig.name
urlpatterns = [
    path('addition_material/create/', AdditionMaterialCreateAPIView.as_view(), name='addition_material-create'),
    path('addition_material/<int:pk>/', AdditionMaterialRetrieveAPIView.as_view(), name='addition_material-get'),
    path('addition_material/list/', AdditionMaterialListAPIView.as_view(), name='addition_material-list'),
    path('addition_material/update/<int:pk>/', AdditionMaterialUpdateAPIView.as_view(),
         name='addition_material-update'),
    path('addition_material/delete/<int:pk>/', AdditionMaterialDestroyAPIView.as_view(),
         name='addition_material-delete'),

    path('topic/create/', TopicCreateAPIView.as_view(), name='topic-create'),
    path('topic/<int:pk>/', TopicRetrieveAPIView.as_view(), name='topic-get'),
    path('topic/list/', TopicListAPIView.as_view(), name='topic-list'),
    path('topic/update/<int:pk>/', TopicUpdateAPIView.as_view(),
         name='topic-update'),
    path('topic/delete/<int:pk>/', TopicDestroyAPIView.as_view(),
         name='topic-delete'),

    path('module/create/', ModuleCreateAPIView.as_view(), name='module-create'),
    path('module/<int:pk>/', ModuleRetrieveAPIView.as_view(), name='module-get'),
    path('module/list/', ModuleListAPIView.as_view(), name='module-list'),
    path('module/update/<int:pk>/', ModuleUpdateAPIView.as_view(),
         name='module-update'),
    path('module/delete/<int:pk>/', ModuleDestroyAPIView.as_view(),
         name='module-delete'),

    path('program/create/', ProgramCreateAPIView.as_view(), name='program-create'),
    path('program/<int:pk>/', ProgramRetrieveAPIView.as_view(), name='program-get'),
    path('program/all/<int:pk>/', ProgramRetrieveAllAPIView.as_view(), name='program-get-all'),
    path('program/list/', ProgramListAPIView.as_view(), name='program-list'),
    path('program/update/<int:pk>/', ProgramUpdateAPIView.as_view(),
         name='program-update'),
    path('program/delete/<int:pk>/', ProgramDestroyAPIView.as_view(),
         name='program-delete'),
]


