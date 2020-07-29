# 3rd party imports
from rest_framework import routers

# Project imports
from .views import TagsViewset

router = routers.DefaultRouter()
router.register('tags', TagsViewset, 'api-tags')

urlpatterns = router.urls
