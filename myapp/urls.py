from django.urls import path,include
from myapp import views

app_name="myapp"

from rest_framework import routers

router=routers.DefaultRouter()
router.register('sampelviewset',views.SampleViewset,basename="sampleviewset")

urlpatterns = [
    path('hello',views.SampleApiView.as_view(),name='SampleApiView'),
    path('',include(router.urls)),
]
