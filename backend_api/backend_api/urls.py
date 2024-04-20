from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sayHello/', include('hello.urls')),  # Include hello app URLs here
]
