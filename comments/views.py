from django.shortcuts import redirect, render
from .models import Comment
from django.contrib import messages
from webpages.models import Post

# Create your views here.
def comments(request):
    if request.method == "POST":
        postid = request.POST['postid']
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']

        post_title = Post.objects.get(id=postid)

        comment_save = Comment(post_title=post_title, name=name, email=email, comment=comment)
        comment_save.save()
        messages.info(request, f'Thank you {name}. Your comment will be posted after reviewing.')
    return redirect('post', id=postid)