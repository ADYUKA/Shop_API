from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from . import models
from . import serializers


@api_view(['GET'])
def category_list_view(request):
    # step 1. collect data from db
    category_list = models.Category.objects.all()

    # step 2. Reformat data from db to DICT(LIST)
    data = serializers.CategorySerializer(instance=category_list, many=True).data

    # step 3. Return as JSON
    return Response(data=data)


@api_view(['GET'])
def category_detail_view(request, id):
    # step 1. collect data from db
    try:
        detail_category = models.Category.objects.get(id=id)
    except models.Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'massage': 'Category not found'})

    # step 2. Reformat data from db to DICT(LIST)
    data = serializers.CategorySerializer(instance=detail_category, many=False).data

    # step 3. Return as JSON
    return Response(data=data)


@api_view(['GET'])
def product_list_view(request):
    # step 1. collect data from db
    product_list = models.Product.objects.all()

    # step 2. Reformat data from db to DICT(LIST)
    data = serializers.ProductSerializer(instance=product_list, many=True).data

    # step 3. Return as JSON
    return Response(data=data)


@api_view(['GET'])
def product_detail_view(request, id):
    # step 1. collect data from db
    try:
        product_detail = models.Product.objects.get(id=id)
    except models.Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'massage': 'Product not found'})

    # step 2. Reformat data from db to DICT(LIST)
    data = serializers.ProductSerializer(instance=product_detail, many=False).data

    # step 3. Return as JSON
    return Response(data=data)


@api_view(['GET'])
def review_list_view(request):
    # step 1. collect data from db
    review_list = models.Review.objects.all()

    # step 2. Reformat data from db to DICT(LIST)
    data = serializers.ReviewSerializer(instance=review_list, many=True).data

    # step 3. Return as JSON
    return Response(data=data)


@api_view(['GET'])
def review_detail_view(request, id):
    # step 1. collect data from db
    try:
        review_detail = models.Review.objects.get(id=id)
    except models.Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'massage': 'Review not found'})

    # step 2. Reformat data from db to DICT(LIST)
    data = serializers.ReviewSerializer(instance=review_detail, many=False).data

    # step 3. Return as JSON
    return Response(data=data)