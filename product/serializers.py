from rest_framework import serializers
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
