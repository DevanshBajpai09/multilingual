from django.contrib import admin
from .models import FAQ
from ckeditor.widgets import CKEditorWidget
from django import forms

class FAQAdminForm(forms.ModelForm):
    answer = forms.CharField(widget=CKEditorWidget())  # ✅ Enable CKEditor for the answer field

    class Meta:
        model = FAQ
        fields = '__all__'

class FAQAdmin(admin.ModelAdmin):
    form = FAQAdminForm  # ✅ Attach the CKEditor form
    list_display = ('question', 'answer')
    search_fields = ('question',)
    fields = ('question', 'answer', 'question_hi', 'question_bn')  # Ensure fields are displayed

admin.site.register(FAQ, FAQAdmin)
