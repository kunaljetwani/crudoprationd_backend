from .models import book, rating, product, order
# from .models import Category, product
from rest_framework import serializers


class bookserializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = "__all__"


# class Categoryerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = "__all__"

class ratingserializer(serializers.ModelSerializer):
    class Meta:
        model = rating
        fields = "__all__"


class productserializer(serializers.ModelSerializer):
    # rating = ratingserializer()

    class Meta:
        model = product
        fields = "__all__"


class orderserializer(serializers.ModelSerializer):
    product = productserializer(many=True)

    class Meta:
        model = order
        fields = "__all__"
