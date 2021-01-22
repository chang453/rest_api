
# from django.shortcuts import render
# from django.views import generic
# from rest_framework import viewsets


from .models import Apidata 
from .serializers import ApiSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView

class api_view(ListAPIView):
    queryset = Apidata.objects.all()
    serializer_class = ApiSerializer


class api_detail_view(RetrieveAPIView):
    lookup_field = 'no'
    queryset = Apidata.objects.all()
    serializer_class = ApiSerializer


class api_update_view(UpdateAPIView):
    lookup_field = 'no'
    queryset = Apidata.objects.all()
    serializer_class = ApiSerializer


class api_delete_view(DestroyAPIView):
    lookup_field = 'no'
    queryset = Apidata.objects.all()
    serializer_class = ApiSerializer

class api_create_view(CreateAPIView):
    queryset = Apidata.objects.all()
    serializer_class = ApiSerializer
