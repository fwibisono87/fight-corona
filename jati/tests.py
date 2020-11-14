from django.test import TestCase

 # Create your tests here.
from django.test import TestCase
from django.urls import resolve, reverse
from django.test import Client
from .models import Pengalaman
from django.apps import apps
from .views import maskermu, listpengalaman
from .forms import FormPengalaman
from .apps import JatiConfig


class ModelTest(TestCase):
    def setUp(self):
        self.pengalaman = Pengalaman.objects.create(cerita_pengalaman="Masker 2 ply")

    def test_instance_created(self):
        self.assertEqual(Pengalaman.objects.count(), 1)

    def test_str(self):
        self.assertEqual(str(self.pengalaman), "Masker 2 ply")


class UrlsTest(TestCase):
    def test_maskermu_use_right_function(self):
        found = resolve('/maskermu/')
        self.assertEqual(found.func, maskermu)

    def test_listpengalaman_use_right_function(self):
        found = resolve('/maskermu/listpengalaman/')
        self.assertEqual(found.func, listpengalaman)


class ViewsTest(TestCase):
    def test_GET_maskermu(self):
        response = Client().get('/maskermu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jati/maskermu.html')

    def test_GET_listpengalaman(self):
        response = Client().get('/maskermu/listpengalaman/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jati/listpengalaman.html')

    def test_POST_maskermu_valid(self):
        response = Client().post('/maskermu/',
                                 {
                                     'cerita_pengalaman': 'Masker 2 ply'
                                 }, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_POST_maskermu_invalid(self):
        response = Client().post('/maskermu/',
                                 {
                                     'cerita_pengalaman': ''
                                 }, follow=True)
        self.assertTemplateUsed(response, 'jati/listpengalaman.html')


class TestApp(TestCase):
    def test_apps(self):
        self.assertEqual(JatiConfig.name, 'jati')
        self.assertEqual(apps.get_app_config('jati').name, 'jati')


