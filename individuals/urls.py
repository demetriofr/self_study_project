from django.urls import path

from .apps import IndividualsConfig
from .views import (
    IndividualCreateAPIView,
    IndividualRetrieveAPIView,
    IndividualListAPIView,
    IndividualUpdateAPIView,
    IndividualDestroyAPIView
)


app_name = IndividualsConfig.name

urlpatterns = [
    path('individual/create/', IndividualCreateAPIView.as_view(), name='individual-create'),
    path('individual/<int:pk>/', IndividualRetrieveAPIView.as_view(), name='individual-get'),
    path('individual/list/', IndividualListAPIView.as_view(), name='individual-list'),
    path('individual/update/<int:pk>/', IndividualUpdateAPIView.as_view(), name='individual-update'),
    path('individual/delete/<int:pk>/', IndividualDestroyAPIView.as_view(), name='individual-delete'),
]
