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
    posts = Post.objects.all()
    return render(request, "forum/forum.html", {"posts": posts})

@require_GET
def get_post(request, postId: str):
    post = Post.objects.get(id=postId)
    return render(request, "forum/forum.html", {"posts": post})

@csrf_exempt
@require_POST
def add_post(request: HttpRequest):
    body = json.loads(request.body)
    name = body.get("name")
    content = body.get("content")
    newPost = Post.objects.create(content=content).save()
    return render(request, "forum/forum.html")