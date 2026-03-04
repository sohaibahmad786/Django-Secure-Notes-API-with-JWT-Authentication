from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import Register_list
from .views import Note_list,Note_detail


urlpatterns = [
    path('login/',TokenObtainPairView.as_view()),
    path('login/refresh/',TokenRefreshView.as_view()),
    path('register/',Register_list.as_view()),
    path('note/',Note_list.as_view()),
    path('note/<int:pk>/',Note_detail.as_view()),

]
