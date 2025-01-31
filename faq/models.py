from django.db import models
from ckeditor.fields import RichTextField
from deep_translator import GoogleTranslator


class FAQ(models.Model):
    objects = None
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.question_hi:
            self.question_hi = GoogleTranslator(source='auto', target='hi').translate(self.question)
        if not self.question_bn:
            self.question_bn = GoogleTranslator(source='auto', target='bn').translate(self.question)
        super().save(*args, **kwargs)

    def get_translated_question(self, lang_code):
        translations = {
            'hi': self.question_hi,
            'bn': self.question_bn,
        }
        return translations.get(lang_code, self.question)

    def __str__(self):
        return self.question

# Create your models here.
