from django.urls import path
from .views import *
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
    path('',realhome,name='realhome'),
    path("nexthome/",home,name="home"),
    path('register/',reg,name="register"),
    path('login/',log,name='login'),
    path('logout/',clogout,name='logout'),
    path('dashboard/',dashboard,name='dashboard'),
    path('about/',about,name='about'),
    path('payments/',pay,name='pay'),
    path('otp/', otp, name='otp'),
    path('profile/',stdprofile, name='profile'),
    path('update_profile/',update_profile,name='update_profile'),
    path("contact/", contact, name="contact"),
    path("addmissionprocess/", admission, name="admissionprocess"),
    path("departments/", departments, name="departments"),
    path("placements/",placements,name="placements"),
    path("activities/",activities,name="activities"),
    path("research/",research,name="research"),
    path("amenities/",amenities,name="amenities"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


