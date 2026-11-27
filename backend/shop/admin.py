from django.contrib import admin
from .models import Category,Product,FAQ,SiteSettings,AboutPage
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
 list_display=("name","slug","is_active","sort_order"); prepopulated_fields={"slug":("name",)}
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
 list_display=("name","category","price","is_available","is_featured"); list_filter=("category","is_available","is_featured"); search_fields=("name","description"); prepopulated_fields={"slug":("name",)}
admin.site.register([FAQ,SiteSettings,AboutPage])
