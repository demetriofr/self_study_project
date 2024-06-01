from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView
)


class UserWithStatusModeratorCreateAPIView(CreateAPIView):
    pass
