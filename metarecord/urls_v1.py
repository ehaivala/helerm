from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from metarecord.views import (ActionViewSet, AttributeViewSet, FunctionViewSet, PhaseViewSet, RecordTypeViewSet,
                              RecordViewSet, TemplateViewSet)

router = DefaultRouter()
router.register(r'function', FunctionViewSet)
router.register(r'phase', PhaseViewSet)
router.register(r'action', ActionViewSet)
router.register(r'record', RecordViewSet)
router.register(r'record_type', RecordTypeViewSet)
router.register(r'attribute', AttributeViewSet)
router.register(r'template', TemplateViewSet, base_name='template')


urlpatterns = [
    url(r'^', include(router.urls, namespace='v1')),
]
