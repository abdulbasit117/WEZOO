from venv import create
from rest_framework.mixins import ListModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin,CreateModelMixin
from rest_framework import mixins,viewsets,response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticatedOrReadOnly,AllowAny
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from .models import Cards,CustomUser, City
from rest_framework.parsers import MultiPartParser,FormParser
from .permisions import IsAdminOrReadOnly,IsOwnerOrReadOnly

from .serializers import CardsSerializer, HotDesksSerializer,RegisterSerializer,LoginSerializer

class CardsViewSet(CreateModelMixin,ListModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin,GenericViewSet):
    permission_classes = [IsOwnerOrReadOnly,IsAuthenticatedOrReadOnly,IsAdminOrReadOnly]
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer
    parser_classes = (MultiPartParser, FormParser)  

class RegisterViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer       
    permission_classes = [AllowAny]


class LoginViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data,context={'request':request})
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data.get('user')
        token,created = Token.objects.get_or_create(user=user)
        return response.Response({"detail":"Вы успешно вошли","token":token.key})
    


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = HotDesksSerializer
    parser_classes = (MultiPartParser, FormParser)  

    

