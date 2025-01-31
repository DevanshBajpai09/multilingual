from rest_framework import generics
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get(self, request, *args, **kwargs):
        lang = request.GET.get('lang', 'en')
        faqs = FAQ.objects.all()
        translated_faqs = [
            {'id': faq.id, 'question': faq.get_translated_question(lang), 'answer': faq.answer}
            for faq in faqs
        ]
        return Response(translated_faqs)
