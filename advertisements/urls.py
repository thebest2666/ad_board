from django.urls import path
from rest_framework.routers import DefaultRouter

from .apps import AdvertisementsConfig
from .views import AdViewSet, ReviewViewSet, AdListAPIView

router = DefaultRouter()
router.register(r'ads', AdViewSet)
router.register(r'reviews', ReviewViewSet)

app_name = AdvertisementsConfig.name

urlpatterns = [
   path('ad_list/', AdListAPIView.as_view(), name='ad_list'),
]

urlpatterns += router.urls