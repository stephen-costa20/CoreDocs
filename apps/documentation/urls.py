from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('details/', views.details, name='details'),
    path('page-editor/', views.page_editor, name='page_editor'),
    
]