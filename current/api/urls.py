from django.urls import path

from . import views

urlpatterns = [
    path('<slug:location>/', views.CurrentModelAPIViewSet.as_view({'get': 'list'}), name='current_api_location'),
    path('<slug:location>/<slug:value_type>/', views.CurrentModelAPIViewSet.as_view({'get': 'retrieve',
                                                                                     'post':  'partial_update',
                                                                                     'put':   'partial_update',
                                                                                     'patch': 'partial_update'
                                                                                     }), name='current_api'),
    path('<slug:location>/<slug:value_type>/delete/', views.CurrentModelAPIViewSet.as_view({ 'delete': 'destroy'}), name='current_api_delete_value'),
]
