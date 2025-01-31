from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer
from django.http import HttpResponse


class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


def get_queryset(self):
    lang_code = self.request.query_params.get('lang', 'en')
    faqs = self.queryset
    if lang_code in ['hi', 'bn']:
        for faq in faqs:
            faq.question = faq.get_translated_question(lang_code)
    return faqs


def home(request):
    return HttpResponse("Welcome to the FAQ API. Visit /admin or /api/faqs.")
