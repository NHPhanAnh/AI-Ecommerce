from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

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
