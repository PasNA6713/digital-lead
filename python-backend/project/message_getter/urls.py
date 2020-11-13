from django.urls import path

from . import views

urlpatterns = [
    # message methods
    path('create/', views.CreateMessageView.as_view()),
    path('get/', views.GetAllMessagesView.as_view()),
    path('get/<int:pk>/', views.GetMessageView.as_view()),
    path('delete/<int:pk>/', views.DeleteMessageView.as_view()),

    # user methods
    path('create-user/', views.CreateUserView.as_view()),
    path('get-user/', views.GetAllUsersView.as_view()),
    path('get-user/<int:pk>/', views.GetUserView.as_view()),
    path('delete-user/<int:pk>/', views.DeleteUserView.as_view()),
]