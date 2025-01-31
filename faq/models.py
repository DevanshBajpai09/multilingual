from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache

translator = Translator()

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)  # Hindi translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation

    def save(self, *args, **kwargs):
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, src='en', dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, src='en', dest='bn').text
        super().save(*args, **kwargs)

    def get_translated_question(self, lang):
        cache_key = f'faq_{self.id}_{lang}'
        cached_translation = cache.get(cache_key)
        if cached_translation:
            return cached_translation
        
        translations = {
            'hi': self.question_hi,
            'bn': self.question_bn
        }
        translated_text = translations.get(lang, self.question)  # Default to English
        cache.set(cache_key, translated_text, timeout=60 * 60)  # Cache for 1 hour
        return translated_text

    def __str__(self):
        return self.question
