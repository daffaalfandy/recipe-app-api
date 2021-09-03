from django.urls import path

from user import views

# THIS VARIABLE FOR REVERSE FUNCTION ON TEST TO BE WORK
app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name="create"),
    path('token/', views.CreateTokenView.as_view(), name='token')
]
