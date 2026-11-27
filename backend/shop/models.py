from django.db import models
class Category(models.Model):
 name=models.CharField(max_length=80,unique=True); slug=models.SlugField(max_length=90,unique=True); description=models.CharField(max_length=240,blank=True); image_url=models.URLField(blank=True); is_active=models.BooleanField(default=True); sort_order=models.PositiveIntegerField(default=0)
 class Meta: ordering=["sort_order","name"]
 def __str__(self): return self.name
class Product(models.Model):
 category=models.ForeignKey(Category,related_name="products",on_delete=models.SET_NULL,null=True,blank=True); name=models.CharField(max_length=160); slug=models.SlugField(max_length=180,unique=True); description=models.TextField(blank=True); price=models.DecimalField(max_digits=10,decimal_places=2); compare_at_price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True); image_url=models.URLField(blank=True); is_featured=models.BooleanField(default=False); is_available=models.BooleanField(default=True); created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True)
 class Meta: ordering=["-is_featured","-created_at"]
 def __str__(self): return self.name
class FAQ(models.Model):
 question=models.CharField(max_length=240); answer=models.TextField(); is_active=models.BooleanField(default=True); sort_order=models.PositiveIntegerField(default=0)
 class Meta: ordering=["sort_order","id"]
 def __str__(self): return self.question
class SiteSettings(models.Model):
 shop_name=models.CharField(max_length=120,default="Sonika"); tagline=models.CharField(max_length=240,blank=True,default="Everyday beauty, little joys."); address=models.TextField(blank=True); phone=models.CharField(max_length=40,blank=True); whatsapp=models.CharField(max_length=40,blank=True); opening_hours=models.TextField(blank=True); google_maps_url=models.URLField(blank=True); latitude=models.DecimalField(max_digits=10,decimal_places=7,null=True,blank=True); longitude=models.DecimalField(max_digits=10,decimal_places=7,null=True,blank=True); instagram_url=models.URLField(blank=True); facebook_url=models.URLField(blank=True); updated_at=models.DateTimeField(auto_now=True)
 def __str__(self): return self.shop_name
class AboutPage(models.Model):
 title=models.CharField(max_length=160,default="A little about our shop"); body=models.TextField(blank=True); image_url=models.URLField(blank=True); updated_at=models.DateTimeField(auto_now=True)
 def __str__(self): return self.title
