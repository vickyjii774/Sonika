from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from shop.views import CategoryViewSet,ProductViewSet,FAQViewSet,SiteSettingsView,AboutView,ImageKitAuthView,health
router=DefaultRouter()
router.register("categories",CategoryViewSet,basename="category")
router.register("products",ProductViewSet,basename="product")
router.register("faqs",FAQViewSet,basename="faq")
urlpatterns=[path("django-admin/",admin.site.urls),path("api/health/",health),path("api/auth/token/",TokenObtainPairView.as_view()),path("api/auth/token/refresh/",TokenRefreshView.as_view()),path("api/settings/",SiteSettingsView.as_view()),path("api/about/",AboutView.as_view()),path("api/imagekit/auth/",ImageKitAuthView.as_view()),path("api/",include(router.urls))]
