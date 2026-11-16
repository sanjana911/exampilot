"""
URL configuration for exampilot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from exam.views import AssessmentListCreateView
from exam.views import AssessmentRetrieveUpdateDeleteView
from accounts.views import AdminCreateView
from problems.views import QuestionCreateView
from problems.views import QuestionRetrieveUpdateDeleteView
from accounts.views import StudentCreateView
from evaluation.views import SubmissionStartView,SubmissionRetrieveView
from evaluation.views import AnswerSubmitView,AnswerUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exam/assessments/',AssessmentListCreateView.as_view()),
    path('exam/assessments/<int:pk>/',AssessmentRetrieveUpdateDeleteView.as_view()),

    #account url

    path('owners/assessments/',AdminCreateView.as_view()),

    #problems url

    path('assesment/<int:pk>/questions/',QuestionCreateView.as_view()),
    path('question/<int:pk>/',QuestionRetrieveUpdateDeleteView.as_view()),
    
    #student registration
    path('student/register/',StudentCreateView.as_view()),

    #submission
    path('assessment/<int:pk>/submission/',SubmissionStartView.as_view()),
    path('submission/<int:pk>/',SubmissionRetrieveView.as_view()),

    #answers
    path('submission/<int:pk>/answer/',AnswerSubmitView.as_view()),
    path('answers/<int:pk>/',AnswerUpdateView.as_view())

]
