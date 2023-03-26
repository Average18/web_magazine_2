from django.urls import path
from . import views

urlpatterns = [
    #path('<slug:slug>/', views.PostListView.as_view(), name='blog'),
    path('', views.index)
]
