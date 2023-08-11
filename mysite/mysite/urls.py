from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "MySite Admin"
admin.site.site_title = "MySite Panel"
admin.site.index_title ="Welcome to MySite Admin Panel"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('portfolio/', include('portfolio.urls')),
    path("__reload__/", include("django_browser_reload.urls")),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)