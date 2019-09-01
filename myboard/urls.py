from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('board/', include('board.urls')),
    path('admin/', admin.site.urls),
]
