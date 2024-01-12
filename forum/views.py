from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from django.shortcuts import render
from forum.models import Post
from django.views.decorators.csrf import csrf_exempt
import json
import uuid

@require_GET
def all_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, "forum/forum.html", {"posts": posts})

@require_GET
def get_post(request, postId: str):
    post = Post.objects.get(id=postId)
    return render(request, "forum/forum.html", {"posts": post})

@csrf_exempt
@require_POST
def add_post(request: HttpRequest):
    content = request.POST.get("content", None)
    newPost = Post.objects.create(content=content).save()
    return HttpResponseRedirect(request.headers.get("Referer"))