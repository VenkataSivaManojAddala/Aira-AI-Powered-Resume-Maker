import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

"""Necessary fields to get data from the user."""

# Name
# Socials - Linkedin, Github, Mail-ID, Mobile number, website
# Summary/Objective
# Education (scalable)
# Projects (Scalable)
# Publications (Scalable)
# Skills (Scalable)
# Languages (Scalable)
# Achievements / Awards (scalable)
# Coursework (Scalable)
# Additional Engagements / Non-Techincal activities (scalable)
# Work Experience (Scalable)
# Certifications (Scalable)


def process_text(text):  
  text = text.replace('•', '  *')
  return text

GOOGLE_API_KEY = 'AIzaSyCM' + 'JASvij_Ai2HfU' + '1Sa8nQeV3-vyoDmV5o'
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

def generate_introduction(information):
    # generates introdcution/about of a user based on his/her tech stack, hobbies and interests.
    response = model.generate_content(f"Generate a Summary/Objective to put in my resume, about myself with the technologies I am familiar with, {information['skills'], information['languages']}. Please dont be informal. Also you need not mention my name and greetings. The output must be a paragraph")
    introduction = process_text(response.text)

    return introduction

def generate_project_descriptions(information):
    # generates project title-description pairs based on given input titles and breifs.
    projects = []

    for project in information["projects"]:
        project_name = project["project_title"]
        project_description = project["desc"]
        response = model.generate_content(f"Generate a 4-5 line description without exaggarating for my project named '{project_name}', here is the brief: \n {project_description}")
        project['desc'] = (response.text)
        projects.append(project)

    return projects


def useai(information):

    try:
        if information['objective'] == "" or information['objective'] == None or not (information['objective']):
            print("Objective empty")
            print(information)
            information['objective'] = generate_introduction(information)
        information['projects'] = generate_project_descriptions(information)
        return information
    except Exception as e:
        return "Oops ! An unkown error has occured."