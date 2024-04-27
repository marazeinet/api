# from django.urls import path, include
# from api import views

# urlpatterns = [
#     path('', views.index, name="index"),
#     path('', include('api.urls')),
# ]


from rest_framework import routers
from .api import ApiViewSet

ruta = routers.DefaultRouter()
ruta.register('api/Empleados', ApiViewSet, 'api')

urlpatterns = ruta.urls