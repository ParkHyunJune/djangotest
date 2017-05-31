from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.models import Post
from blog.forms import PostCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

def main_view(request):

    post = Post.objects.all()

    # for post in posts:
    #     print(post.title)

    context = {
        'posts':post
    }

    return render(request, 'post/post-list.html', context)

# def main_view2(request):
#     return HttpResponse('메인뷰투투투투 음아')

def post_add_view(request):
    if request.method == 'GET':
        form = PostCreationForm()

        context = {
            'forms':form
        }
        return render(request, 'post/post-add.html', context)

    elif request.method == 'POST':
        form = PostCreationForm(request.POST)


        if form.is_valid():
            author = User.objects.first()
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']

            Post.objects.create (
                author = author,
                title = title,
                text = text,
            )
        return redirect('post_main')

    # 1. post_add_view(request) 함수를 만든다
    # 2. url 이름은 postadd 잘 연결 되었는지 확인한다