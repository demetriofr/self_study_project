from django.urls import path

from workplaces.apps import WorkplacesConfig
from workplaces.views import (
    SOUTCardCreateAPIView,
    SOUTCardRetrieveAPIView,
    SOUTCardListAPIView,
    SOUTCardUpdateAPIView,
    SOUTCardDestroyAPIView
)


app_name = WorkplacesConfig.name

urlpatterns = [
    path('sout_card/create/', SOUTCardCreateAPIView.as_view(), name='sout_card-create'),
    path('sout_card/<int:pk>/', SOUTCardRetrieveAPIView.as_view(), name='sout_card-get'),
    path('sout_card/list/', SOUTCardListAPIView.as_view(), name='sout_card-list'),
    path('sout_card/update/<int:pk>/', SOUTCardUpdateAPIView.as_view(), name='sout_card-update'),
    path('sout_card/delete/<int:pk>/', SOUTCardDestroyAPIView.as_view(), name='sout_card-delete'),
]
