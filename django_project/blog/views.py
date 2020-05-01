from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMs',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 27, 2020'
    },
    {
        'author': 'RenoMs',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'August 28, 2020'
    }
]




def home(request):
    context = {
        #variabel 'posts' that is called by home.html
        'posts': posts
    }
    return render(request, 'blog/home.html', context)



def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
