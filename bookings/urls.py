# urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('seat_data/', views.seat_data, name='seat_data'),
    path('reserve_seat/<int:seat_id>/', views.reserve_seat, name='reserve_seat'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
