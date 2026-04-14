import threading
import requests
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

def notify_ai_service():
    def _fire():
        try:
            requests.post('http://ai-chat-service:8005/api/refresh_kb', timeout=5)
        except Exception as e:
            print(f"Failed to notify AI service: {e}")
    threading.Thread(target=_fire).start()

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        q = self.request.query_params.get('q', None)
        category = self.request.query_params.get('category', None)
        if q is not None:
            queryset = queryset.filter(name__icontains=q)
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset

    def perform_create(self, serializer):
        super().perform_create(serializer)
        notify_ai_service()

    def perform_update(self, serializer):
        super().perform_update(serializer)
        notify_ai_service()

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        notify_ai_service()
