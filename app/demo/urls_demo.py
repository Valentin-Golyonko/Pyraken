from django.urls import path
from demo.views import DemoPageView, CheckCeleryAjax

urlpatterns = [
    path('', DemoPageView.as_view(), name='demo-page'),
    path('check-celery-ajax/', CheckCeleryAjax.as_view(), name='check-celery-ajax'),
]
