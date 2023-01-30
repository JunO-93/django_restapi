from django.urls import include, path
from rest_framework import routers
# from cube_history.views import DataViewSet, apiViewSet
from cube_history import views

# router = routers.DefaultRouter()
# router.register(r'data', DataViewSet)
# router.register(r'apiView', apiViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('valueInput/', views.valueInputSet), 
    path('valueInput/selectCubeData/', views.selectCubeData, name='selectCubeData'),
]