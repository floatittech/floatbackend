from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from floatapp import views
from floatapp.views import UserScreenshotsListView, ShareWorkflowListView, ScreenshotViewSet
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register('userdetail', views.UserDetailViewSet, basename="UserDetail")
router.register('ss', ScreenshotViewSet, basename="ss")

urlpatterns = [
    path('admin-float/', admin.site.urls), # Django Admin Login
    path('api/', include(router.urls)), # EndPoint Prefix For Default Router
    path('api/screenshots/<uuid:workflow_id>/', UserScreenshotsListView.as_view(), name="screenshot_list"), # Our own views.py EndPoint
    path('api/share/<uuid:pk>/', ShareWorkflowListView.as_view(), name="ShareWorkflow"), # Our own views.py EndPoint
    path("api/auth/", include("dj_rest_auth.urls")),  # endpoints provided by dj-rest-auth
    path("api/social/login/", include("floatapp.urls")),  # our own views
    path("accounts/", include("allauth.urls")),  # endpoints provided by allauth

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
