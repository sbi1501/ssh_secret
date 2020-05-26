from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('teams/', views.TeamListView.as_view(), name='teams'),
    path('team/<int:pk>', views.TeamDetailView.as_view(), name='team-detail'),
    path('my-secrets/', views.MySecretListView.as_view(), name='my-secrets'),
    path('my-secret/<uuid:pk>', views.MySecretDetailView.as_view(), name='my-secret-detail'),
]
