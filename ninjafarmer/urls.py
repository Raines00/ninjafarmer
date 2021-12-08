from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings
import farm
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('farm.urls', namespace='farm') )
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)