from django.shortcuts import render
from django.http import HttpResponse

posts = [

    {
        'Author' : 'Pavan Hapse',
        'Title' : 'Blog Post',
        'Content' : 'This is my first content for blog',
        'date_posted' : 'August 18th 2023'
    },

    {
        'Author' : 'Pavan Hapse',
        'Title' : 'Detail about blog',
        'content' : 'This is my second content',
        'date_posted' : 'August 19th 2023'
    }

]


def Home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'Blog_home.html', context)

def About(request):
    return render(request, 'about.html', {'title' : 'about'})
