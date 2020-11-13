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

class EventField(serializers.Field):
    def to_internal_value(self, data):
        logger.debug(data)
        return Ml.classify(data)

    def to_representation(self, value):
        return value

    def get_default(self):
        return self.to_internal_value('1')

class DangerField(serializers.Field):
    def to_internal_value(self, data):
        return Ml.get_danger_level(data)

    def to_representation(self, value):
        return value

    def get_default(self):
        return self.to_internal_value('1')

class CreateMessageSerializer(serializers.ModelSerializer):
    author_id = UserField()
    # event_class = EventField(required=False)
    # danger_level = DangerField(required=False)
    event_class = serializers.HiddenField(default=Ml.classify('self'))
    danger_level = serializers.HiddenField(default=Ml.get_danger_level('1'))

    class Meta:
        model = MessageModel
        exclude = ['author']
