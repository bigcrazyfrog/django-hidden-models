from django.test import TestCase

from .models import Article


class VisibleManagerTestCase(TestCase):
    def setUp(self) -> None:
        Article.objects.create()
        Article.objects.create()

    def test_default_visible_manager(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(), 2)

        qs.hide()
        qs = Article.objects.all()
        self.assertEqual(qs.count(), 0)

    def test_visible_all_manager(self):
        qs = Article.all_objects.all()
        self.assertEqual(qs.count(), 2)

        qs.hide()
        qs = Article.all_objects.all()
        self.assertEqual(qs.count(), 2)

        qs.show()
        qs = Article.all_objects.all()
        self.assertEqual(qs.count(), 2)

    def test_visible_hidden_manager(self):
        Article.objects.all().hide()

        qs = Article.hidden_objects.all()
        self.assertEqual(qs.count(), 2)

        qs.show()
        qs = Article.hidden_objects.all()
        self.assertEqual(qs.count(), 0)

