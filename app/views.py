from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.status import HTTP_400_BAD_REQUEST

from .models import Category, SubCategory, Product
from .serializers import (GetProductSerializer, GetProductByCategorySerializer,
	GetProductBySubCategorySerializer,GetSubCategoryByCategorySerializer,
	AddProductsSerializer, GetCategoriesSerializer)

class GetCategoriesViewSet(viewsets.ModelViewSet):
	serializer_class = GetCategoriesSerializer
	queryset = Category.objects.all()

class GetProductViewSet(viewsets.ModelViewSet):
	serializer_class = GetProductSerializer
	queryset = Product.objects.all()

class GetProductByCategoryView(APIView):
	def get(self, request, format=None):
		param = request.query_params
		queryset = Product.objects.filter(category__category=param["param"])
		serializer = GetProductByCategorySerializer(queryset, many=True)
		return Response(serializer.data)

class GetProductBySubCategoryView(APIView):
	def get(self, request, format=None):
		param = request.query_params
		queryset = Product.objects.filter(subcategory__subcategory=param["param"])
		serializer = GetProductBySubCategorySerializer(queryset, many=True)
		return Response(serializer.data)

class GetSubCategoryByCategoryView(APIView):
	def get(self, request, format=None):
		param = request.query_params
		queryset = SubCategory.objects.filter(category__category=param["param"])
		serializer = GetSubCategoryByCategorySerializer(queryset, many=True)
		return Response(serializer.data)

class AddProducts(APIView):
	serializer_class = AddProductsSerializer
	def post(self, request, format=None):
		data = request.data
		serializer = AddProductsSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			new_data = serializer.data
			return Response(new_data)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
