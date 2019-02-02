from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('submit', views.submit, name='submit'),
    path('information/<id_no>', views.information, name='information'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
