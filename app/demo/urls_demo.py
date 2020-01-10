from demo.views import DemoPageView, CheckCeleryAjax, OneCpuCeleryAjax, FourCpuCeleryAjax
from django.urls import path

urlpatterns = [
    path('', DemoPageView.as_view(), name='demo-page'),
    path('api/check-celery-ajax/', CheckCeleryAjax.as_view(), name='check-celery-ajax'),
    path('1cpu-celery-ajax/', OneCpuCeleryAjax.as_view(), name='1cpu-celery-ajax'),
    path('4cpu-celery-ajax/', FourCpuCeleryAjax.as_view(), name='4cpu-celery-ajax'),
]
