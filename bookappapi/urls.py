from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register('book', BookViewsets, basename='book')

urlpatterns = [
    path('book<int:pk>/', GenericBookView.as_view()),
    path('', include(router.urls))
]