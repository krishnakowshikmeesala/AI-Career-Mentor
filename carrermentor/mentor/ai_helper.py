import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_career_report(student):
    prompt = f"""
    You are an expert AI Career Mentor.

    Name: {student.full_name}
    Age: {student.age}
    Education: {student.education}
    Location: {student.location}
    Interests: {student.interests}
    Strengths: {student.strengths}
    Career Goal: {student.career_goal}
    Learning Preference: {student.learning_preference}
    Challenge: {student.challenge}
    Dream Career: {student.dream_career}

    Generate:
    1. Recommended Career
    2. Why This Career
    3. Match Score out of 100
    4. Skills To Learn
    5. Six Month Roadmap
    6. Free Learning Resources
    """

    response = model.generate_content(prompt)

    return response.text
