from django.urls import path

from . import views

urlpatterns = [
    path('pages/',views.ListDashboard.as_view(),name = 'create'),
    path('pages/<int:pk>/',views.DetailDashboard.as_view(),name = 'details'),
]
