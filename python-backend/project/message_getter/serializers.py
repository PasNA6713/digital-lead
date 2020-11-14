import json

from rest_framework import serializers

from .models import UserIdentifierModel, MessageModel, AddressModel
from .model import classify as Ml

from loguru import logger


class UserIdentifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserIdentifierModel
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressModel
        fields = '__all__'

class GetMessageSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    author = UserIdentifierSerializer()

    class Meta:
        model = MessageModel
        fields = '__all__'


class UserField(serializers.Field):
    def to_internal_value(self, data):
        obj = UserIdentifierModel.objects.get_or_create(id=data)
        return data

    def to_representation(self, value):
        return value


class CreateMessageSerializer(serializers.ModelSerializer):
    author_id = UserField()
    my_address = serializers.DictField(required=False)
    date = serializers.DateTimeField(required=False)
    address = serializers.SlugRelatedField(slug_field="text", read_only=True)
    danger_level = serializers.ReadOnlyField()
    event_class = serializers.ReadOnlyField()

    def create(self, validated_data):
        ModelClass = self.Meta.model
        address = validated_data.pop('my_address')
        if address:
            validated_data['address'] = AddressModel.objects.get_or_create(
                latitude=address.get('latitude'),
                longtitude=address.get('longtitude'),
                text=Ml.find_address(validated_data.get('text'))
                )[0]
        else: 
            validated_data['address'] = AddressModel.objects.get_or_create(text=Ml.find_address(validated_data.get('text')))[0]
        validated_data['event_class'] = Ml.classify(validated_data.get('text'))
        validated_data['danger_level'] = Ml.get_danger_level(validated_data.get('text'))
        instance = ModelClass._default_manager.create(**validated_data)
        return instance

    class Meta:
        model = MessageModel
        exclude = ['author']