from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Post
from .serializers import PostSerializer


@require_http_methods(["GET"])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
@require_http_methods(["POST"])
def post_create(request):
    data = JSONParser().parse(request)

    # Check for existing 'url'
    if 'url' in data and Post.objects.filter(url=data['url']).exists():
        return JsonResponse({'error': 'Duplicate entry found'}, status=400) 

    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'message': 'Post created successfully'}, status=201)
    return JsonResponse(serializer.errors, status=400)

@require_http_methods(["GET"])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Post not found'}, status=404)

    serializer = PostSerializer(post)
    return JsonResponse(serializer.data)

@csrf_exempt
@require_http_methods(["PUT", "PATCH"])
def post_update(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Post not found'}, status=404)

    data = JSONParser().parse(request)
    serializer = PostSerializer(post, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'message': 'Post updated successfully'}, status=200)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@require_http_methods(["DELETE"])
def post_delete(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Post not found'}, status=404)

    post.delete()
    return JsonResponse({'message': 'Post deleted successfully'}, status=204)

@require_http_methods(["GET"])
def post_query(request):
    query_params = request.GET
    # Add validation or sanitization of query_params as needed
    posts = Post.objects.filter(**query_params.dict())
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False)