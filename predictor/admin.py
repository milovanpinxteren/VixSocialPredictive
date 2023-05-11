from django.contrib import admin

# Register your models here.
from predictor.models import Banks, KeyWords


@admin.register(Banks)
class BanksAdmin(admin.ModelAdmin):
    list_display = ['bank_name']

@admin.register(KeyWords)
class KeyWordsAdmin(admin.ModelAdmin):
    list_display = ["bank", 'keyword']