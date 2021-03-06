from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.api.v1.viewsets import SignupViewSet, LoginViewSet, HomePageViewSet, CustomTextViewSet

router = DefaultRouter()
router.register('signup', SignupViewSet, base_name='signup')
router.register('login', LoginViewSet, base_name='login')
router.register('customtext', CustomTextViewSet)
router.register('homepage', HomePageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
