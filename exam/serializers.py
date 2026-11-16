from rest_framework import serializers
from exam.models import Assesment
from datetime import datetime
from problems.models import Question
from problems.serializers import QuestionSerializer

from django.db.models import Sum

class AssessmentSerializer(serializers.ModelSerializer):

    date = serializers.SerializerMethodField(read_only =True)

    question_count = serializers.SerializerMethodField(read_only = True)

    total_marks = serializers.SerializerMethodField(read_only = True)

    questions = serializers.SerializerMethodField(read_only = True)

    class Meta:

        model = Assesment

        fields =  "__all__"

        read_only_fields =["id","end_time","is_active"]

    def validate(self, validated_data):

        duration = validated_data.get("duration")

        exam_date = validated_data.get("exam_date")

        cur_date = datetime.now().date()

        if exam_date < cur_date:

            raise serializers.ValidationError("invalid date, date should be greater than current date")

        if duration not in range(1,6):

            raise serializers.ValidationError("invalid duration, duration should be in the range of 1 to 5")

        return validated_data

    def get_date(self, obj):

        return datetime.now()


    def get_question_count(self,obj):

        return Question.objects.filter(assesment=obj).count()


    def get_total_marks(self, obj):

        return Question.objects.filter(assesment = obj).values("score").aggregate(total = Sum("score")).get("total")

    def get_questions(self,obj):
        
        question_object = Question.objects.filter(assesment = obj)

        serializer_instance = QuestionSerializer(question_object, many = True)

        return serializer_instance.data



