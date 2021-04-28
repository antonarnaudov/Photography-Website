from rest_framework import serializers

from Api.serializers.photos_serializer import ShowPhotosSerializer
from Api.serializers.user_serializer import UserSimpleSerializer
from Photos.models.wishes_model import Wishes


class ShowWishesSerializer(serializers.ModelSerializer):
    """

    """
    # check the user serializers
    user = UserSimpleSerializer()
    photo = ShowPhotosSerializer()

    class Meta:
        model = Wishes
        fields = '__all__'
        # depth goes within the relations
        depth = 1


class CreateWishesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishes
        fields = '__all__'
