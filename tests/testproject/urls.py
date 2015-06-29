from django.conf.urls import patterns, url, include
from django.contrib import admin
from rest_framework.routers import SimpleRouter
from .views import TestResourceViewSet

admin.autodiscover()

router = SimpleRouter()
router.register(r'test-resources', TestResourceViewSet)

urlpatterns = patterns(
    '',
    url(r'', include(router.urls)),
)
