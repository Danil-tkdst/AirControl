from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mainapp.api.urls')),
    path('', include('mainapp.urls'))
]
