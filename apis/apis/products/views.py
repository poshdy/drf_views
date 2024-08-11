from rest_framework.response import Response
from .serializer import ProductSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Product
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ViewSet


# API VIEWS
class ProductListCreateAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        validated_data = serializer.validated_data
        serializer.create(validated_data=validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, id):
        product = Product.objects.get(pk=id)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        product = Product.objects.get(pk=id)
        serializer = ProductSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        validated_data = serializer.validated_data
        serializer.update(instance=product, validated_data=validated_data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        Product.objects.filter(pk=id).delete()

        return Response("product deleted!")


# GENERIC VIEWS
class ProductListCreateGAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateRetrieveDestoryGAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"


# class ProductUpdateRetrieveApi(RetrieveUpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = "slug"


# class ProductListView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class ProductCreateView(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class ProductRetrieve(RetrieveAPIView):
#     lookup_field = "slug"
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class ProductUpdate(UpdateAPIView):
#     lookup_field = "slug"
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


class ProductViewSet(ViewSet):
    lookup_field = "slug"

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        validated_data = serializer.validated_data
        serializer.create(validated_data=validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, slug):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, slug=slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, slug):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, slug=slug)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(product, serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, slug):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, slug=slug)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.update(product, serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, slug):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, slug=slug)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
