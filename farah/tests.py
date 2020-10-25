# from django.test import TestCase

# # Create your tests here.
# from django.test import TestCase
# from django.urls import resolve, reverse
# from django.test import Client
# from .models import Kegiatan
# from django.apps import apps
# from .views import edukasi, listkegiatan
# from .forms import FormKegiatan
# from .apps import FarahConfig


# class ModelTest(TestCase):
#     def setUp(self):
#         self.kegiatan = Kegiatan.objects.create(nama_kegiatan="Belajar")
       
#     def test_instance_created(self):
#         self.assertEqual(Kegiatan.objects.count(), 1)

#     def test_str(self):
#         self.assertEqual(str(self.kegiatan), "Belajar")


# class UrlsTest(TestCase):

#     def setUp(self):
#         self.kegiatan = Kegiatan.objects.create(nama_kegiatan="Belajar Bersama")
#         self.edukasi = reverse("edukasi")
#         self.listkegiatan = reverse("listkegiatan")
      
#     def test_edukasi_use_right_function(self):
#         found = resolve(self.edukasi)
#         self.assertEqual(found.func, edukasi)

#     def test_listkegiatan_use_right_function(self):
#         found = resolve(self.listkegiatan)
#         self.assertEqual(found.func, listkegiatan)


# class TestApp(TestCase):
#     def test_apps(self):
#         self.assertEqual(FarahConfig.name, 'farah')
#         self.assertEqual(apps.get_app_config('farah').name, 'farah')


# class ViewsTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.edukasi = reverse("edukasi")
#         self.listkegiatan = reverse("listkegiatan")

#     def test_GET_edukasi(self):
#         response = self.client.get(self.index)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'farah/edukasi.html')

#     def test_GET_listkegiatan(self):
#         response = self.client.get(self.listkegiatan)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'farah/listkegiatan.html')


#     def test_POST_edukasi(self):
#         response = self.client.post(self.edukasi,
#                                     {
#                                         'nama_kegiatan': 'Belajar Bersama'
#                                     }, follow=True)
#         self.assertEqual(response.status_code, 200)

#     def test_POST_addkegiatan_invalid(self):
#         response = self.client.post(self.edukasi,
#                                     {
#                                         'nama_kegiatan': ''
#                                     }, follow=True)
#         self.assertTemplateUsed(response, 'farah/listkegiatan.html')
