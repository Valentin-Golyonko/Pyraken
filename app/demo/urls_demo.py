from django.urls import path
from demo.views import DemoPageView

urlpatterns = [
    path('', DemoPageView.as_view(), name='demo-page'),
]
