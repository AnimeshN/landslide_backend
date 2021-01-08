"""uttarkashi_earthquake URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from predictor import views

# [Rockstate,Hydrology,Weathering,Overburden_Depth,Erosion,Rainfall,Road_Influence,Joint_failure,River_Bank_failure,Toe_failure]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/<str:Geomorphology>/<str:RochChar>/<str:OverburdenThickness>/<str:Hydrology>/<str:Erosion>/<str:Rainfall>/<str:Anthropogenic>/<str:SlopeType>/<str:LandslideMaterial>/<str:Movement>/<str:Style>', views.descisionTree.as_view(), name='earthquake'),
]
