
from django.urls import path,include
from . import views
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from Blog_API.views import PostViewSet

router = DefaultRouter()
router.register('post', PostViewSet, basename='post')

urlpatterns = [
    # path('', views.index),
    # path('<int:pk>/', views.post_detail),
    path('', include(router.urls)),
    path('<int:pk>/', include(router.urls)),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]