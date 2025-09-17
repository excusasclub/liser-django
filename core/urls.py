from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('baglist/<int:baglist_id>/', views.baglist_detail, name='baglist_detail'),
]
