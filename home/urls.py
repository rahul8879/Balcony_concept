from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:tour_slug>/', views.package_details, name='package_details'),
    path('test/quote_submit', views.quote_submit, name="quote_submit"),
    path('capture_location/', views.capture_location, name='capture_location'),
    path('<slug>/submit_booking', views.submit_booking, name='submit_booking')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
