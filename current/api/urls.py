from django.urls import path

from . import views

urlpatterns = [
    path('', views.CurrentLocationListAPIView.as_view(), name='current_api_list'),
    path('<slug:location>/', views.CurrentModelAPIViewSet.as_view({'get': 'list'}), name='current_api_location'),
    path('<slug:location>/<slug:value_type>/', views.CurrentModelAPIViewSet.as_view({ 'get': 'retrieve'}), name='current_api_get_value'),
    path('<slug:location>/<slug:value_type>/create/', views.CurrentModelAPIViewSet.as_view({ 'put': 'update'}), name='current_api_create'),
    path('<slug:location>/<slug:value_type>/update/', views.CurrentModelAPIViewSet.as_view({ 'patch': 'partial_update'}), name='current_api_set_value'),
    path('<slug:location>/<slug:value_type>/delete/', views.CurrentModelAPIViewSet.as_view({ 'delete': 'destroy'}), name='current_api_delete_value'),
]
