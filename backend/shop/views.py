import hashlib,hmac,secrets,time
from django.conf import settings
from django.http import JsonResponse
from rest_framework import viewsets,serializers
from rest_framework.permissions import AllowAny,IsAdminUser,SAFE_METHODS
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Category,Product,FAQ,SiteSettings,AboutPage
def health(request): return JsonResponse({"status":"ok","service":"sonika-api"})
class AdminWriteViewSet(viewsets.ModelViewSet):
 def get_permissions(self): return [AllowAny()] if self.request.method in SAFE_METHODS else [IsAdminUser()]
class CategoryViewSet(AdminWriteViewSet):
 queryset=Category.objects.filter(is_active=True); lookup_field="slug"
 class S(serializers.ModelSerializer):
  class Meta: model=Category; fields="__all__"
 serializer_class=S
class ProductViewSet(AdminWriteViewSet):
 serializer_class=None; lookup_field="slug"
 class S(serializers.ModelSerializer):
  category_name=serializers.CharField(source="category.name",read_only=True)
  class Meta: model=Product; fields="__all__"
 serializer_class=S
 def get_queryset(self):
  q=Product.objects.select_related("category")
  if self.request.method in SAFE_METHODS: q=q.filter(is_available=True)
  if self.request.query_params.get("category"): q=q.filter(category__slug=self.request.query_params["category"])
  if self.request.query_params.get("search"): q=q.filter(name__icontains=self.request.query_params["search"])
  if self.request.query_params.get("featured")=="true": q=q.filter(is_featured=True)
  return q
class FAQViewSet(AdminWriteViewSet):
 queryset=FAQ.objects.filter(is_active=True)
 class S(serializers.ModelSerializer):
  class Meta: model=FAQ; fields="__all__"
 serializer_class=S
class SingletonView(APIView):
 model=None; serializer_class=None
 def obj(self):
  x=self.model.objects.first()
  return x or self.model.objects.create()
 def get(self,request): return Response(self.serializer_class(self.obj()).data)
 def patch(self,request):
  if not request.user.is_staff: return Response({"detail":"Admin access required."},status=403)
  s=self.serializer_class(self.obj(),data=request.data,partial=True); s.is_valid(raise_exception=True); s.save(); return Response(s.data)
 def put(self,request): return self.patch(request)
class SiteSettingsView(SingletonView):
 model=SiteSettings
 class S(serializers.ModelSerializer):
  class Meta: model=SiteSettings; fields="__all__"; read_only_fields=("updated_at",)
 serializer_class=S
class AboutView(SingletonView):
 model=AboutPage
 class S(serializers.ModelSerializer):
  class Meta: model=AboutPage; fields="__all__"; read_only_fields=("updated_at",)
 serializer_class=S
class ImageKitAuthView(APIView):
 permission_classes=[IsAdminUser]
 def get(self,request):
  if not settings.IMAGEKIT_PUBLIC_KEY or not settings.IMAGEKIT_PRIVATE_KEY: raise ValidationError("ImageKit credentials are not configured.")
  token=secrets.token_urlsafe(24); expire=int(time.time())+1800
  signature=hmac.new(settings.IMAGEKIT_PRIVATE_KEY.encode(),f"{token}{expire}".encode(),hashlib.sha1).hexdigest()
  return Response({"token":token,"expire":expire,"signature":signature,"publicKey":settings.IMAGEKIT_PUBLIC_KEY})
