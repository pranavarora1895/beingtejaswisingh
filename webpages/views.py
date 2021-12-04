from django.shortcuts import render

# Create your views here.
def home(request):
    data = {'home_page': "active"}
    return render(request, 'webpages/home.html', data)

def about(request):
    data = {'about_us_page': "active"}
    return render(request, 'webpages/about.html', data)

def post(request):
    return render(request, 'webpages/post.html')

def contact(request):
    data = {'contact_page': "active"}
    return render(request, 'webpages/contact.html', data)
