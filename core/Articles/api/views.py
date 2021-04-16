from Articles.models import Article,Author
from Articles.api.serializer import ArticleSerializer,AuthorSerializer,AvatarSerializer

from rest_framework import generics
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework import mixins
from Articles.api.permissions import ProfilOrReadOnly,ArticleAuthorOrReadOnly


from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly


from rest_framework import filters

class AuthorViewSet(mixins.ListModelMixin,mixins.UpdateModelMixin,
mixins.RetrieveModelMixin,GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated,ProfilOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['user_name__username']


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated,ArticleAuthorOrReadOnly]

   
    def get_queryset(self):
        queryset = Article.objects.all()
        username = self.request.query_params.get('username',None) 
        if username is not None:
            queryset = queryset.filter(author__user_name__username = username) 
        return queryset


  
    def perform_create(self, serializer): 
        author = self.request.user.profil 
        serializer.save(author=author)

    
    filter_backends=[filters.SearchFilter] 
    search_fields = ['title','article','author__city','author__user_name__username'] 


class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class= AvatarSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profil_obj = self.request.user.profil
        return profil_obj



