from rest_framework import serializers
from .models import Category, SubCategory, Product

class GetCategoriesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('id', 'category')

class GetProductSerializer(serializers.ModelSerializer):
	category = serializers.StringRelatedField()
	subcategory = serializers.StringRelatedField()
	class Meta:
		model = Product
		fields = ('id', 'name', 'category', 'subcategory')

class GetProductByCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('id', 'name')

class GetProductBySubCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('id', 'name')

class GetSubCategoryByCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = SubCategory
		fields = ('id', 'subcategory')

class AddProductsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('id', 'name', 'category', 'subcategory')

		def create(self, validated_data):
			return Product.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.name =  validated_data.get('name', instance.name)
			instance.category = validated_data.get('category', instance.category)
			instance.subcategory = validated_data.get('subcategory', instance.subcategory)
			instance.save()
			return instance

