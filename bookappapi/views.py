from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class GenericBookView(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin,
                      mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = BookSerializer
    queryset =Book.objects.all()
    lookup_field = 'pk'
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class BookViewsets(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                   mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    serializer_class = BookSerializer
    queryset = Book.objects.all()