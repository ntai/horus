from django.urls import path

from . import views

urlpatterns = [
    path('', views.ValueTypeModelAPIViewSet.as_view({'get': 'list'}), name='value_type_api_list'),
    path('<slug:slug>/', views.ValueTypeModelAPIViewSet.as_view({'get': 'retrieve'}), name='value_type_api_details'),
    path('<slug:slug>/update/', views.ValueTypeModelAPIViewSet.as_view({ 'put': 'update', 'patch': 'partial_update'}), name='value_type_api_update'),
    path('<slug:slug>/delete/', views.ValueTypeModelAPIViewSet.as_view({ 'delete': 'destroy'}), name='value_type_api_delete'),
]
