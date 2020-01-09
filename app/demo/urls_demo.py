from django.urls import path
from demo.views import DemoPageView, CheckCeleryAjax, OneCpuCeleryAjax, FourCpuCeleryAjax

urlpatterns = [
    path('', DemoPageView.as_view(), name='demo-page'),
    path('check-celery-ajax/', CheckCeleryAjax.as_view(), name='check-celery-ajax'),
    path('1cpu-celery-ajax/', OneCpuCeleryAjax.as_view(), name='1cpu-celery-ajax'),
    path('4cpu-celery-ajax/', FourCpuCeleryAjax.as_view(), name='4cpu-celery-ajax'),
]
