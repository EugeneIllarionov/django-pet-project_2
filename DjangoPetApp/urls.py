from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from DjangoPetApp.settings import MEDIA_URL, MEDIA_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('profiles.urls')),
    path('', include('news.urls'))
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

