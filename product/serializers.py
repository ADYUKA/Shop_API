from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from . import models


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = models.Category
        fields = 'name product_count'.split()


    def get_product_count(self, obj):
        return obj.products.count()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'

class ProductReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = models.Product
        fields = 'title description price category reviews rating'.split()

    def get_rating(self, object):
        sum_stars = sum(review.stars for review in object.reviews.all())
        count_reviews = object.reviews.count()
        if count_reviews > 0:
            return sum_stars / count_reviews
        else:
            return 0


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=64)
    description = serializers.CharField(required=False)
    price = serializers.IntegerField()
    category_id = serializers.IntegerField(min_value=1)

    def validate_category_id(self, category_id):
        try:
            models.Category.objects.get(id=category_id)
        except models.Category.DoesNotExist:
            raise ValidationError('Category does not exist!')
        return category_id


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    stars = serializers.IntegerField(min_value=1, max_value=5)
    product_id = serializers.IntegerField(min_value=1)

    def validate_product_id(self, product_id):
        try:
            models.Product.objects.get(id=product_id)
        except models.Product.DoesNotExist:
            raise ValidationError('Product does not exist!')
        return product_id