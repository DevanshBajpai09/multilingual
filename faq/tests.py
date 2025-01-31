from django.test import TestCase
from .models import FAQ

class FAQTestCase(TestCase):
    def setUp(self):
        FAQ.objects.create(question="What is Django?", answer="Django is a Python framework.")

    def test_translation_fallback(self):
        faq = FAQ.objects.get(question="What is Django?")
        self.assertEqual(faq.get_translated_question('fr'), "What is Django?")  # Should return English as fallback
