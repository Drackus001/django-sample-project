from django.shortcuts import render
from pages.demo import myname
from .models import Post

# posts = [
#     {
#         'author' : 'Satyam Agarwal',
#         'title' : 'Blog 1',
#         'content' : 'Content for first blog',
#         'date_posted': 'December 03, 1998'
#     },
#     {
#         'author' : 'Rick Grimes',
#         'title' : 'Blog 2',
#         'content' : 'Content for Second blog',
#         'date_posted': 'November 23, 2008'
#     }
# ]

# Create your views here.
# def home(request):
#     return render(request,"home.html",{"title":"HOME"})#used for passing values to html pages

# def about(request):
#     ABOUT = "ABOUT"
#     context = {
#         'users' : users,
#         'title' : ABOUT
#     }
#     return render(request,"about.html",context)



def home(request):
    
    return render(request,"home.html",{"title":"HOME"})

def about(request):
    context = {
    
        'title': "ABOUT"
        
    }
    return render(request,"about.html",context)