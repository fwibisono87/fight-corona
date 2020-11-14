# Create your tests here.
from django.test import TestCase
from django.urls import resolve, reverse
from django.test import Client
from .models import Kegiatan
from django.apps import apps
from .views import edukasi, listkegiatan
from .forms import FormKegiatan
from .apps import FarahConfig


class ModelTest(TestCase):
    def setUp(self):
        self.kegiatan = Kegiatan.objects.create(nama_kegiatan="Belajar")
       
    def test_instance_created(self):
        self.assertEqual(Kegiatan.objects.count(), 1)

    def test_str(self):
        self.assertEqual(str(self.kegiatan), "Belajar")


class UrlsTest(TestCase):
    def test_edukasi_use_right_function(self):
        found = resolve('/edukasi/')
        self.assertEqual(found.func, edukasi)

    def test_listkegiatan_use_right_function(self):
        found = resolve('/edukasi/listkegiatan/')
        self.assertEqual(found.func, listkegiatan)


class ViewsTest(TestCase):
    def test_GET_edukasi(self):
        response = Client().get('/edukasi/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'farah/edukasi.html')

    def test_GET_listkegiatan(self):
        response = Client().get('/edukasi/listkegiatan/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'farah/listkegiatan.html')

    def test_POST_edukasi_valid(self):
        response = Client().post('/edukasi/',
                                    {
                                        'nama_kegiatan': 'Belajar'
                                    }, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_POST_edukasi_invalid(self):
        response = Client().post('/edukasi/',
                                    {
                                        'nama_kegiatan': ''
                                    }, follow=True)
        self.assertTemplateUsed(response, 'farah/listkegiatan.html')

class TestApp(TestCase):
    def test_apps(self):
        self.assertEqual(FarahConfig.name, 'farah')
        self.assertEqual(apps.get_app_config('farah').name, 'farah')