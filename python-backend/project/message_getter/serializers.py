from loguru import logger

from rest_framework import serializers

from .models import UserIdentifierModel, MessageModel
from .model import classify as Ml

from loguru import logger


class GetMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = '__all__'

class UserIdentifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserIdentifierModel
        fields = '__all__'


class UserField(serializers.Field):
    def to_internal_value(self, data):
        obj = UserIdentifierModel.objects.get_or_create(id=data)
        return data

    def to_representation(self, value):
        return value

class CreateMessageSerializer(serializers.ModelSerializer):
    author_id = UserField()

    def create(self, validated_data):
        ModelClass = self.Meta.model
        validated_data['event_class'] = Ml.classify(validated_data.get('text'))
        validated_data['danger_level'] = Ml.get_danger_level(validated_data.get('text'))
        validated_data['address'] = Ml.find_address(validated_data.get('text'))
        instance = ModelClass._default_manager.create(**validated_data)
        return instance

    class Meta:
        model = MessageModel
        exclude = ['author', 'event_class', 'danger_level', 'address']
