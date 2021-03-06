"""GTInfo URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from iu_api.views import UserOnlineActivityObjectViewSet, TrackedUserObjectViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'user_online_activity_object', UserOnlineActivityObjectViewSet, basename="UserOnlineActivityObject")
router.register(r'tracked_user_object', TrackedUserObjectViewSet)


urlpatterns = [
    path('iu_api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include("start_page.urls")),
    path('', include("auth_pages.urls")),
    path('', include("account.urls")),
    path('', include("visualisation.urls")),
    path('', include("subscription.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
