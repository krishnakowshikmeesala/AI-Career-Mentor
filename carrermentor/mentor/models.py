from django.db import models

class StudentAssessment(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    education = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    interests = models.TextField()
    strengths = models.TextField()
    career_goal = models.CharField(max_length=100)
    learning_preference = models.CharField(max_length=100)
    challenge = models.CharField(max_length=200)
    dream_career = models.CharField(max_length=100)
    recommended_career = models.CharField(max_length=100,blank=True)
    match_score = models.IntegerField(default=0)    
    recommended_skills = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name