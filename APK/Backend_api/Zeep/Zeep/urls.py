"""
URL configuration for Zeep project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
import Stamp.views 

from  rest_framework import routers
from  Stamp.views  import Admin_PatternStamp,Read_PatternStamp

router = routers.SimpleRouter()
from Stamp.views  import Admin_PatternStamp,Read_PatternStamp
router.register('stamp/admin_PatternStamp',Admin_PatternStamp,basename="Admin-PatternStamp")
router.register('stamp/read_PatternStamp',Read_PatternStamp,basename="Read-PatternStamp")





urlpatterns = [
    path('admin/', admin.site.urls),
    path('stamp/',include('Stamp.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', Stamp.views.profile,name='account_profile'),
    path('', Stamp.views.profile,name='home'),
    path('api/',include(router.urls)),
    
    
    #path('',include('Stamp.urls')),
    
]


