from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('', model_form_upload, name='upload'),
    path('home/', homeview, name='home'),
    path('download/<int:pk>/', DownloadView.as_view()),
    path('download_all/', DownloadAllView.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)