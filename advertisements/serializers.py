from rest_framework.serializers import ModelSerializer

from advertisements.models import Ad, Review


class AdSerializer(ModelSerializer):
    """
        Сериализатор вывода объявления
    """

    class Meta:
        model = Ad
        fields = ('title', 'description', 'price', 'created_at')


class ReviewSerializer(ModelSerializer):
    """
        Сериализатор вывода отзыва
    """

    class Meta:
        model = Review
        fields = "__all__"