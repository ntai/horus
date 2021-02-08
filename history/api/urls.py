from django.urls import path

from . import views

urlpatterns = [
    # path('', views.HistoryModelAPIViewSet.as_view({'get': 'list'}), name='current_api_list'),
    path('<slug:location>/', views.HistoryModelAPIViewSet.as_view({'get': 'list'}), name='current_api_list_location'),
    path('<slug:location>/<slug:value_type>/', views.HistoryModelAPIViewSet.as_view({ 'get': 'retrieve'}), name='current_api_get_value'),
    path('<slug:location>/<slug:value_type>/update/', views.HistoryModelAPIViewSet.as_view({ 'put': 'update', 'patch': 'partial_update'}), name='current_api_set_value'),
    path('<slug:location>/<slug:value_type>/delete/', views.HistoryModelAPIViewSet.as_view({ 'delete': 'destroy'}), name='current_api_delete_value'),
]
