from django.test import TestCase, Client
from .models import Image
import mock
from django.core.files import File




class mainPageTest(TestCase):
    def test_mainpage_exists(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_mainpage_uses_base_html(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'global/base.html')

    def test_mainpage_uses_home_html(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'global/home.html')

    def test_mainpage_has_welcome(self):
        response = Client().get('')
        self.assertContains(response, "Selamat Datang Di")


class forumPageTest(TestCase):
    def test_forum_index_exists(self):
        response = Client().get('/forum')
        self.assertEqual(response.status_code, 200)

    def test_forum_index_uses_base_html(self):
        response = Client().get('/forum')
        self.assertTemplateUsed(response, 'global/base.html')

    def test_forum_index_uses_index_html(self):
        response = Client().get('/forum/new_post')
        self.assertTemplateUsed(response, 'francis/upload_form.html')

    def test_make_model_forum(self):
        image_obj = Image.objects.create(
            title="Lorem ipsum dolor sit amet, consectetur porttitor.",
            author="cicero lagi",
            caption="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse pharetra congue nisl, non ornare tortor convallis non. Suspendisse potenti. Maecenas maximus eget magna nec luctus. In hac habitasse platea dictumst. Donec libero laoreet."
        )

    def test_check_model_forum(self):
        image_obj = Image.objects.create(
            title="Lorem ipsum dolor sit amet, consectetur porttitor.",
            author="cicero lagi",
            caption="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse pharetra congue nisl, non ornare tortor convallis non. Suspendisse potenti. Maecenas maximus eget magna nec luctus. In hac habitasse platea dictumst. Donec libero laoreet."
        )
        self.assertEqual(image_obj.title,  "Lorem ipsum dolor sit amet, consectetur porttitor.")
        self.assertEqual(image_obj.__str__(), "Lorem ipsum dolor sit amet, consectetur porttitor.")

    def test_views_forum(self):
        file_mock = mock.MagicMock(spec=File, name='FileMock')
        response = Client().post("forum/new_post", follow=True, form={
            'title': "ini lorem ipsum",
            'author': 'cicero lmao',
            'email': 'cicero@gov.gr',
            'caption': 'panjaaaaang',
            'image': file_mock
        })


# Create your tests here.
