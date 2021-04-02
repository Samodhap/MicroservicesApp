from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products
from .serializers import ProductCatalogSerializer


# Create your views here.
@api_view(['GET'])
def view_products(request):
    if request.method == 'GET':  # user requesting data
        products = Products.objects.all()
        serializer = ProductCatalogSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def view_detailed_product(request, pk):
    try:
        product = Products.objects.get(product_serial_num=pk)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':  # user requesting data
        serializer = ProductCatalogSerializer(product, many=False)
        return Response(serializer.data)


@api_view(['POST'])
def add_products(request):
    if request.method == 'POST':  # user posting data
        serializer = ProductCatalogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_product(request, pk):
    try:
        product = Products.objects.get(product_serial_num=pk)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        product_update = ProductCatalogSerializer(product, data=request.data)
    if product_update.is_valid():
        product_update.save()
        return Response(product_update.data,status=status.HTTP_204_NO_CONTENT)
    return Response(product_update.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_product(request,pk):
    try:
        product = Products.objects.get(product_serial_num=pk)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
