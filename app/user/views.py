from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import UserSerializer, AuthTokenSerializer

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer
    print("serializer_class:" , serializer_class)

class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for a user """
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    print('serializer_class:{0}, renderer_classes:{1}'.format(serializer_class, renderer_classes))
# What is  ObtainAuthToken AuthTokenSerializer

class ManageUserView(generics.RetrieveUpdateAPIView):
    """ Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    
    def get_object(self):
        """ Retrieve and return authentication user"""
        return self.request.user
