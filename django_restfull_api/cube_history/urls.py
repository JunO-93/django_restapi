from django.urls import include, path
from rest_framework import routers
from cube_history import views

urlpatterns = [
    # path('', include(router.urls)),
    path('valueInput/', views.valueInputSet), 
    path('valueInput/selectCubeData/', views.selectCubeData, name='selectCubeData'),
    path('viewCubeInfo/',views.viewCubeInfo), 
]