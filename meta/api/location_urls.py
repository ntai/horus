from django.urls import path

from . import views

urlpatterns = [
    path('', views.LocationModelAPIViewSet.as_view({'get': 'list'}), name='location_api_list'),
    path('<slug:slug>/', views.LocationModelAPIViewSet.as_view({'get': 'retrieve'}), name='location_api_details'),
    path('<slug:slug>/update/', views.LocationModelAPIViewSet.as_view({ 'put': 'update', 'patch': 'partial_update'}), name='location_api_update'),
    path('<slug:slug>/delete/', views.LocationModelAPIViewSet.as_view({ 'delete': 'destroy'}), name='location_api_delete'),
]
