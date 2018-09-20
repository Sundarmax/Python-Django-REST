from rest_framework.viewsets import ModelViewSet
from .serializers import postSerializer
from .models import post

class PostViewSet(ModelViewSet):
    queryset = post.objects.all()
    serializer_class = postSerializer