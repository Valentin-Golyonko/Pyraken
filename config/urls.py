from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/core/', include('app.core.urls_core')),

    path('admin/', admin.site.urls),
]
