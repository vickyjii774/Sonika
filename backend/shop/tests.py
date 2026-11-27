from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from .models import Product, SiteSettings

class StoreApiTests(APITestCase):
    def test_public_settings_are_available(self):
        response = self.client.get("/api/settings/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["shop_name"], "Sonika")
        self.assertTrue(SiteSettings.objects.exists())

    def test_public_product_list_is_available(self):
        response = self.client.get("/api/products/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_anonymous_user_cannot_create_product(self):
        response = self.client.post("/api/products/", {
            "name": "Rose Lip Tint", "slug": "rose-lip-tint", "price": "350.00"
        }, format="json")
        self.assertIn(response.status_code, (401, 403))
        self.assertFalse(Product.objects.exists())

    def test_staff_user_can_create_product(self):
        User = get_user_model()
        admin = User.objects.create_user(username="shopadmin", password="test-pass-123", is_staff=True)
        self.client.force_authenticate(user=admin)
        response = self.client.post("/api/products/", {
            "name": "Rose Lip Tint", "slug": "rose-lip-tint", "price": "350.00",
            "description": "A lightweight everyday tint."
        }, format="json")
        self.assertEqual(response.status_code, 201, response.data)
        self.assertTrue(Product.objects.filter(slug="rose-lip-tint").exists())

    def test_staff_can_update_shop_location(self):
        User = get_user_model()
        admin = User.objects.create_user(username="settingsadmin", password="test-pass-123", is_staff=True)
        self.client.force_authenticate(user=admin)
        response = self.client.patch("/api/settings/", {
            "address": "Kathmandu, Nepal",
            "google_maps_url": "https://www.google.com/maps/embed?pb=test"
        }, format="json")
        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(response.data["address"], "Kathmandu, Nepal")
