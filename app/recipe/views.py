from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Ingredient, Recipe

from recipe import serializers


class BasicRecipeAttrViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user = self.request.user)

# class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin): explain what the difference is?
class TagViewSet(BasicRecipeAttrViewSet):
    """Manage tags in the database"""

    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class IngredientViewSet(BasicRecipeAttrViewSet):
    """Manage Ingredients in the database"""

    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes=(TokenAuthentication, )
    permission_classes=(IsAuthenticated, )

    def get_queryset(self):
        """Retrieve the recipes for the authenticated user"""
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        """Return appropriate serializer class""" #  can also be used with if self.request.user.is_staff:
        if self.action == 'retrieve':
            #print("1", serializers.RecipeDetailSerializer.data, self.action, serializers.RecipeDetailSerializer)
            return serializers.RecipeDetailSerializer
        #print("2", self.serializer_class.data, self.action, self.serializer_class)
        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new recipe"""
        serializer.save(user=self.request.user)



        