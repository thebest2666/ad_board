from rest_framework.routers import DefaultRouter

from .apps import AdvertisementsConfig
from .views import AdViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'ads', AdViewSet)
router.register(r'reviews', ReviewViewSet)

app_name = AdvertisementsConfig.name

urlpatterns = router.urls