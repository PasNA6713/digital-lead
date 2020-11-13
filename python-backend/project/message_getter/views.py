from datetime import datetime

from rest_framework.generics import (
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    ListAPIView
)
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import UserIdentifierModel, MessageModel
from .serializers import UserIdentifierSerializer, GetMessageSerializer, CreateMessageSerializer
from .filters import MessageFilter
from .services import get_file

from loguru import logger


# Upload File and check it
class UploadPhotoView(APIView):
    def post(self, request, format=None):
        get_file(request.FILES['file'])
        return Response(status=status.HTTP_200_OK)

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

    # добавляем время запроса в выдачу, чтобы делать последующие запросы, начиная с заданного момента
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        response = serializer.data
        response.append(datetime.now())
        return Response(response)