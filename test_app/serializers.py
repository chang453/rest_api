from .models import Apidata
from rest_framework import serializers

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apidata
        fields = ('no', 'contents', 'datetime', 'title', 'url')



# class ApiDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Apidata
#         fields = ('no', 'contents')



# class ApiCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Apidata
#         fields = ('no', 'contents', 'datetime', 'title', 'url')