from django.shortcuts import render, redirect
from .models import StudentAssessment
from .ai_helper import generate_career_report


def home(request):
    return render(request, 'home.html')
def assessment(request):
    if request.method == "POST":
        interests = request.POST.getlist('interests')
        strengths = request.POST.getlist('strengths')
        student = StudentAssessment.objects.create(
            full_name=request.POST['full_name'],
            age=request.POST['age'],
            education=request.POST['education'],
            location=request.POST['location'],
            interests=", ".join(interests),
            strengths=", ".join(strengths),
            career_goal=request.POST['career_goal'],
            learning_preference=request.POST['learning_preference'],
            challenge=request.POST['challenge'],
            dream_career=request.POST['dream_career']
        )
        report = generate_career_report(student)
        return render(request,"result.html",{"student": student,"report": report})
    return render(request, 'assessment.html')