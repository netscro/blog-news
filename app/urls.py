"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

from news.views import PostViewSet, CategoryViewSet, CommentViewSet

# schema for swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Blog-News",
      default_version='v1',
      description="",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)

# urls for drf
router = routers.DefaultRouter()
router.register(r"category-api",
                CategoryViewSet,)
router.register(r"posts-api",
                PostViewSet,)
router.register(r"comments-api",
                CommentViewSet,)


urlpatterns = [
    path("", TemplateView.as_view(template_name="main_page.html"),
         name='home'),
    path("test/", TemplateView.as_view(template_name="test_drf_api.html"),
         name='test'),
    path("auth/", TemplateView.as_view(template_name="o_auth.html"),
         name='oauth'),


    path("admin/", admin.site.urls),

    # drf main page
    path("drf/", include(router.urls)),

    # swagger page
    url(r'^swagger(?P<format>\.json|\.yaml)',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    url(r'^redoc/', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),

    path("ckeditor/", include("ckeditor_uploader.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
