
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from Blog_API.views import PostViewSet

router = DefaultRouter()
router.register('post', PostViewSet, basename='post')

urlpatterns = [
    # path('', views.index),
    # path('<int:pk>/', views.post_detail),
    # path('generic/article/', views.GenericApiView.as_view(), name='generic'),
    path('', include(router.urls)),
    path('<int:pk>/', include(router.urls)),
]