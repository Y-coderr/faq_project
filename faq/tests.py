from django.test import TestCase
import pytest
from .models import FAQ


@pytest.mark.django_db
def test_faq_creation():
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a high-level Python web framework."
    )
    assert faq.question == "What is Django?"
    assert faq.answer == "Django is a high-level Python web framework."
# Create your tests here.
