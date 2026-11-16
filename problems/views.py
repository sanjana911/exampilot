from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import  Response
from rest_framework import permissions, authentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView


from problems.models import Question
from problems.serializers import QuestionSerializer
from exam.models import Assesment

# Create your views here.


class QuestionCreateView(ListAPIView,CreateAPIView):

    authentication_classes =[authentication.BasicAuthentication]

    permission_classes = [permissions.IsAdminUser]

    serializer_class = QuestionSerializer

    queryset = Question.objects.all()

    def post(self, request, pk = None):
        
        assesment_object = get_object_or_404(Assesment, id = pk)

        form_data = request.data

        serializer_instance = QuestionSerializer(data = form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(assesment = assesment_object)

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)


class QuestionRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    serializer_class = QuestionSerializer

    queryset = Question.objects.all()

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes =[permissions.IsAdminUser]


    def put(self, request, pk = None):

        instance = get_object_or_404(Question, id = pk)

        form_data = request.data

        serializer_instance = QuestionSerializer(data = form_data, instance = instance)

        if serializer_instance.is_valid():
            
            serializer_instance.save()
            
            return Response(serializer_instance.data)
        
        else:
            
            return Response(serializer_instance.errors)


    def delete(self, request, pk = None):
        
        instance = get_object_or_404(Question, id = pk)
    
        instance.delete()
    
        return Response({"message":"deleted.."})



