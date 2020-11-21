from django.urls import path
from rest_framework import routers

from app.core.views import DrawFlagAPIView

router = routers.DefaultRouter()
# router.register('some_view_set', SomeViewSet, basename='some_view_set')

urlpatterns = router.urls

urlpatterns += [
    path('draw_flag/', DrawFlagAPIView.as_view(), name='draw_flag'),
]
