from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

@csrf_exempt
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data)

@csrf_exempt
def post_create(request):
    data = request.body
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'message': 'Post created successfully'}, status=201)
    return JsonResponse({'error': 'Invalid data'}, status=400)

@csrf_exempt
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    serializer = PostSerializer(post)
    return JsonResponse(serializer.data)

@csrf_exempt
def post_update(request, pk):
    post = Post.objects.get(pk=pk)
    data = request.body
    serializer = PostSerializer(post, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'message': 'Post updated successfully'}, status=200)
    return JsonResponse({'error': 'Invalid data'}, status=400)

@csrf_exempt
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return JsonResponse({'message': 'Post deleted successfully'}, status=204)

@csrf_exempt
def post_query(request, query):
    posts = Post.objects.filter(**query)
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data)
