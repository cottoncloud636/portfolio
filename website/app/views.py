from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')
 
projs=[
    {'id':1, 'name':'Kickball League (individual)', 'image':'/static/assets/media/spring-boot.jpg'},
    {'id':2, 'name':'Airbite (group project)', 'image':'/static/assets/media/airbite.png'},
    {'id':3, 'name':'Language Modeling (individual)', 'image':'/static/assets/media/NLP.jpg'},
    {'id':4, 'name':'GameDev (group project)', 'image':'/static/assets/media/gamedev.png'},
]

def projects(request):
    # context = [
    #     {'url':'project/1', 'label':'GUI in Java', 'image_url':'/static/assets/media/candles.jpg'},
    #     {'url':'project/2', 'label':'Socket Programming', 'image_url':'/static/assets/media/airbite.png'},
    #     {'url':'project/3', 'label':'full-stack Java Website_1', 'image_url':'/static/assets/media/airbite.png'}
    # ]
    return render(request, 'projects.html', {'projects': projs}) #"projectlist" is the name of how
                                            #we want to address it in template, "projects": to specify 
                                            #what we are passing in
    
def project(request, pk):
    return render(request, "project.html") 

def contact(request):
    return render(request, 'contact.html') 