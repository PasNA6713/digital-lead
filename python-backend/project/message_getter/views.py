from django.shortcuts import render

from rest_framework.generics import (
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    ListAPIView
)
from django_filters.rest_framework import DjangoFilterBackend

from .models import UserIdentifierModel, MessageModel
from .serializers import UserIdentifierSerializer, GetMessageSerializer, CreateMessageSerializer
from .filters import MessageFilter

from loguru import logger


# User methods
class CreateUserView(CreateAPIView):
    queryset = UserIdentifierModel.objects.all()
    serializer_class = UserIdentifierSerializer

class GetUserView(RetrieveAPIView):
    queryset = UserIdentifierModel.objects.all()
    serializer_class = UserIdentifierSerializer

class DeleteUserView(DestroyAPIView):
    queryset = UserIdentifierModel.objects.all()
    serializer_class = UserIdentifierSerializer

class GetAllUsersView(ListAPIView):
    queryset = UserIdentifierModel.objects.all()
    serializer_class = UserIdentifierSerializer

# Message methods
class CreateMessageView(CreateAPIView):
    queryset = MessageModel.objects.all()
    serializer_class = CreateMessageSerializer

class GetMessageView(RetrieveAPIView):
    queryset = MessageModel.objects.all()
    serializer_class = GetMessageSerializer

class DeleteMessageView(DestroyAPIView):
    queryset = MessageModel.objects.all()
    serializer_class = GetMessageSerializer

class GetAllMessagesView(ListAPIView):
    queryset = MessageModel.objects.all()
    serializer_class = GetMessageSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MessageFilter