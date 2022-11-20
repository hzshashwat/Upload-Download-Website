from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('', model_form_upload, name='upload'),
    path('home', homeview, name='home')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)