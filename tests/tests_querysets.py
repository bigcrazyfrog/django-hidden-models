from django.test import TestCase

from .models import Article


class VisibleModelCase(TestCase):

    model = Article

    def setUp(self) -> None:
        self.model.objects.create(name='model1')
        self.model.objects.create(name='model2')

    def test_hide_queryset(self):
        hided_objects_count = self.model.objects.filter(name='model1').hide()
        self.assertEqual(hided_objects_count, 1)

        hided_objects_count = self.model.objects.all().hide()
        self.assertEqual(hided_objects_count, 1)

        hided_objects_count = self.model.objects.all().hide()
        self.assertEqual(hided_objects_count, 0)

    def test_show_queryset(self):
        self.model.objects.all().hide()

        showed_objects_count = self.model.hidden_objects.filter(name='model1').show()
        self.assertEqual(showed_objects_count, 1)

        showed_objects_count = self.model.hidden_objects.all().show()
        self.assertEqual(showed_objects_count, 1)

        showed_objects_count = self.model.hidden_objects.all().show()
        self.assertEqual(showed_objects_count, 0)
