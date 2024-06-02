"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import getenv

from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Self-study project API",
        default_version="v1",
        description="API for the Self-study project",
        terms_of_service="https://github.com/demetriofr/self_study_project/blob/main/LICENSE.md",
        contact=openapi.Contact(email=getenv('CSU_EMAIL')),
        license=openapi.License(name="MIT License"),

    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('individuals/', include('individuals.urls', namespace='individuals')),
    path('company/', include('company.urls', namespace='company')),
    path('workplaces/', include('workplaces.urls', namespace='workplaces')),

    path('users/', include('users.urls', namespace='users')),

    path('planning/', include('planning.urls', namespace='planning')),
    path('materials/', include('materials.urls', namespace='materials')),
    path('knowledge_testing/', include('knowledge_testing.urls', namespace='knowledge_testing')),

    path('api-auth/', include('rest_framework.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='shema-swagger-ui'),
]
