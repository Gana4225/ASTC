from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [
    path('select1/',home, name='select1'),
    path("cnfm/",cnfm,name='cnfm'),
    path("pay/", pay, name="pay"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


app_name = 'payments'
