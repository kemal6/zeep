from django.urls import path,include
from .views import api_view, initioll,affol

from  rest_framework import routers
from  Stamp.views  import Admin_PatternStamp,Read_PatternStamp,Admin_Monture,Read_Monture

router = routers.SimpleRouter()
from Stamp.views  import Admin_PatternStamp,Read_PatternStamp
router.register('admin_PatternStamp',Admin_PatternStamp,basename="Admin-PatternStamp")
router.register('read_PatternStamp',Read_PatternStamp,basename="Read-PatternStamp")
router.register('admin_Monture',Admin_Monture,basename="Admin-Monture")
router.register('read_Monture',Read_Monture,basename="Read-Monture")

urlpatterns = [
    path('', include(router.urls)),
]
