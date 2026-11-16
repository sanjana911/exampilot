from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime,time,timedelta
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import authentication, permissions

from exam.models import Assesment
from exam.serializers import AssessmentSerializer


# Create your views here.

class AssessmentListCreateView(ListAPIView,CreateAPIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAdminUser]

    serializer_class = AssessmentSerializer

    queryset = Assesment.objects.all()
    

    def post(self,request):

        form_data = request.data

        serializer_instance = AssessmentSerializer(data = form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data
            
            exam_date = cleaned_data.get("exam_date")

            start_time = cleaned_data.get("start_time")

            duration = cleaned_data.get("duration")

            end_date_time = datetime.combine(exam_date, start_time) + timedelta(hours=duration)

            end_time = end_date_time.time()

            serializer_instance.save(end_time= end_time)

            return Response(serializer_instance.data , status=status.HTTP_201_CREATED)

        else:

            return Response(serializer_instance.errors , status= status.HTTP_400_BAD_REQUEST)
        


class AssessmentRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAdminUser]

    serializer_class = AssessmentSerializer

    queryset = Assesment.objects.all()


    def put(self, request, pk = None):

        form_data = request.data

        instance = get_object_or_404(Assesment, id = pk)

        serializer_instance = AssessmentSerializer(data = form_data, instance = instance)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            exam_date = cleaned_data.get("exam_date")

            start_time = cleaned_data.get("start_time")

            duration = cleaned_data.get("duration")

            end_date_time = datetime.combine(exam_date, start_time) + timedelta(hours=duration)

            end_time = end_date_time.time()

            cleaned_data["end_time"]=  end_time

            serializer_instance.save()
            
            return Response(serializer_instance.data, status=status.HTTP_200_OK)

        else:

            return Response(serializer_instance.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk = None):

        instance = get_object_or_404(Assesment, id = pk)

        instance.delete()

        return Response({"message":"deleted.."}, status= status.HTTP_200_OK)

