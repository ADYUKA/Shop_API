from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from . import models
from . import serializers


@api_view(['GET', 'POST'])
def category_list_view(request):
    if request.method == 'GET':
        # step 1. collect data from db
        category_list = models.Category.objects.all()

        # step 2. Reformat data from db to DICT(LIST)
        data = serializers.CategorySerializer(instance=category_list, many=True).data

        # step 3. Return as JSON
        return Response(data=data)

    if request.method == 'POST':
        # 1 step. GET data from request(body)
        name = request.data.get('name')

        # 2 step. Create film by client data
        category = models.Category.objects.create(
            name=name
        )

        # 3 step. Return to client created data
        return Response(data={'category_id': category.id},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_view(request, id):
    # step 1. collect data from db
    try:
        detail_category = models.Category.objects.get(id=id)
    except models.Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'massage': 'Category not found'})

    if request.method == 'GET':
        # step 2. Reformat data from db to DICT(LIST)
        data = serializers.CategorySerializer(instance=detail_category, many=False).data

        # step 3. Return as JSON
        return Response(data=data)

    if request.method == 'PUT':
        detail_category.name = request.data.get('name')
        detail_category.save()

        return Response(data={'category_id': detail_category.id},
                        status=status.HTTP_201_CREATED)

    if request.method == 'DELETE':
        detail_category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def product_list_view(request):
    if request.method == 'GET':
        # step 1. collect data from db
        product_list = models.Product.objects.all()

        # step 2. Reformat data from db to DICT(LIST)
        data = serializers.ProductSerializer(instance=product_list, many=True).data

        # step 3. Return as JSON
        return Response(data=data)

    if request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category_id = request.data.get('category_id')

        product = models.Product.objects.create(
            title=title, description=description, price=price, category_id=category_id
        )
        return Response(data={'product_id': product.id}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_view(request, id):
    # step 1. collect data from db
    try:
        product_detail = models.Product.objects.get(id=id)
    except models.Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'massage': 'Product not found'})

    if request.method == 'GET':
        # step 2. Reformat data from db to DICT(LIST)
        data = serializers.ProductSerializer(instance=product_detail, many=False).data

        # step 3. Return as JSON
        return Response(data=data)

    if request.method == 'PUT':
        product_detail.title = request.data.get('title')
        product_detail.description = request.data.get('description')
        product_detail.price = request.data.get('price')
        product_detail.category_id = request.data.get('category_id')
        product_detail.save()

        return Response(data={'product_id': product_detail.id}, status=status.HTTP_201_CREATED)

    if request.method == 'DELETE':
        product_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def review_list_view(request):
    if request.method == 'GET':
        # step 1. collect data from db
        review_list = models.Review.objects.all()

        # step 2. Reformat data from db to DICT(LIST)
        data = serializers.ReviewSerializer(instance=review_list, many=True).data

        # step 3. Return as JSON
        return Response(data=data)

    if request.method == 'POST':
        text = request.data.get('text')
        stars = request.data.get('stars')
        product_id = request.data.get('product_id')

        review = models.Review.objects.create(
            text=text, stars=stars, product_id=product_id
        )
        return Response(data={'review_id': review.id}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, id):
    # step 1. collect data from db
    try:
        review_detail = models.Review.objects.get(id=id)
    except models.Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'massage': 'Review not found'})

    if request.method == 'GET':
        # step 2. Reformat data from db to DICT(LIST)
        data = serializers.ReviewSerializer(instance=review_detail, many=False).data

        # step 3. Return as JSON
        return Response(data=data)

    if request.method == 'PUT':
        review_detail.text = request.data.get('text')
        review_detail.stars = request.data.get('stars')
        review_detail.product_id = request.data.get('product_id')
        review_detail.save()

        return Response(data={'review_id': review_detail.id}, status=status.HTTP_201_CREATED)

    if request.method == 'DELETE':
        review_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def product_reviews_list_view(request):
    if request.method == 'GET':
        product_list = models.Product.objects.all()
        data = serializers.ProductReviewsSerializer(instance=product_list, many=True).data

        return Response(data=data)