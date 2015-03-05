import json
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from user_mgmt.models import MyUser
from user_mgmt.serializers import UserSerializer


# Login View
class LoginView(APIView):

    def get(self, request):
        if request.user.is_authenticated():
            print "authenticated"
            return render(request, 'user_mgmt/base.html', {'id': request.user.id})
        else:
            print "Unauthenticated"
            return render(request, 'user_mgmt/base.html')

    def post(self, request):
        # Ad-hoc solution for getting data from request.body
        param_dict = json.loads(request.body)
        email = param_dict.get('email')
        password = param_dict.get('password')
        my_user = authenticate(email=email, password=password)
        if my_user is not None:
            if my_user.is_active:
                login(request, my_user)
                data = {'id': my_user.id}
                return Response(data=data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


# Registration View
class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = MyUser.objects.all()


# Logout View
class LogoutView(APIView):

    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)