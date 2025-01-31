from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer
from django.http import HttpResponse


class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


def home(request):
    return HttpResponse("Welcome to the FAQ API. Visit /admin or /api/faqs.")
