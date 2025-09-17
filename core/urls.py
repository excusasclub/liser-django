from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('baglists/', views.baglist_edition, name='baglist_edition'),
    path('baglists/<int:baglist_id>/', views.baglist_detail, name='baglist_detail'),
]