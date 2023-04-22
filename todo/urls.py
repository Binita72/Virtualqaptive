from rest_framework import routers
from .views import TodoView

router = routers.DefaultRouter()
router.register(r'api/tasks', TodoView, 'task')

urlpatterns = router.urls