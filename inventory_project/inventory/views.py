
# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer
from rest_framework import filters

## @api_view(['GET'])
##def product_list(request):
  ##  products=Product.objects.all()
    ##serializer=ProductSerializer(products,many=True)
    ##return Response(serializer.data)

##@api_view(['GET'])
##ef api_root(request):
  ##  return Response({
    ##    "message":"Inventory Management API",
      ##  "available_endpoints":{
        ##    "products":"/api/products/"
       ## }
    ##})
class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes=[IsAuthenticated]

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']