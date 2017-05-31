from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post
# Create your views here.

def main_view(request):

    post = Post.objects.all()

    # for post in posts:
    #     print(post.title)

    context = {
        'posts':post
    }

    return render(request, 'base/base.html', context)

# def main_view2(request):
#     return HttpResponse('메인뷰투투투투 음아')

def post_add_view(request):
    # 1. post_add_view(request) 함수를 만든다
    # 2. url 이름은 postadd 잘 연결 되었는지 확인한다



