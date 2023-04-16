import profile
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from base.models import PostModel,Profile
from .serializers import PostSerializer,UserSerializer,ProfileSerializer
from django.contrib.auth.models import User
from .permissions import IsSuperUser, IsAuthorOrReadOnly, IsStaffOrReadOnly

class PostListApi(ListAPIView):
    queryset = PostModel.objects.all() 
    serializer_class = PostSerializer
    
class PostCreateApi(CreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    
    
class PostUpdateApi(RetrieveUpdateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, IsStaffOrReadOnly)
    
    
class PostDetailApi(RetrieveAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, IsStaffOrReadOnly)
    
    
class PostDeleteApi(RetrieveDestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, IsStaffOrReadOnly)

class PostEditApi(RetrieveUpdateDestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (IsAuthorOrReadOnly, IsStaffOrReadOnly)
   
class UserEdit(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)
    
    
class CreateUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)
    
class ProfileDetailApi(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthorOrReadOnly, IsStaffOrReadOnly)
    
class ProfileUpdateApi(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthorOrReadOnly, IsStaffOrReadOnly)