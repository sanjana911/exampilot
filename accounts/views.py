from django.shortcuts import render
from django.contrib.auth.models import User


from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import AdminSerializer

# Create your views here.

class AdminCreateView(CreateAPIView):

    serializer_class = AdminSerializer

    queryset = User.objects.all()

    def post(self, request):

        form_data = request.data

        serializer_instance = AdminSerializer(data = form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            instance = User.objects.create_superuser(**cleaned_data)

            serializer_instance = AdminSerializer(instance)

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)


class StudentCreateView(APIView):

    def post(self, request):

        form_data = request.data

        serializer_instance = AdminSerializer(data = form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            instance = User.objects.create_user(**cleaned_data)

            serializer_instance = AdminSerializer(instance)

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)
