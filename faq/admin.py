from django.contrib import admin
from .models import FAQ


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)
    search_fields = ('question',)

# Register your models here.
# this project is developed by Yash Kadam(Y-coderr)
