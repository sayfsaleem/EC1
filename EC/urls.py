from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404, handler500
# from client.views import custom_error, handler404, handler500

urlpatterns = [
    path('froala_editor/', include('froala_editor.urls')),
    path('admin/', admin.site.urls),
    path('',include('client.urls')),
]
handler404 = 'client.views.handler404'
handler500 = 'client.views.handler500'
