from rest_framework.response import Response
from .serializers import *
from rest_framework import viewsets, generics
from .models import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import action
import blurhash

# Create your views here.

class GoogleLoginView(SocialLoginView):
    authentication_classes = [] # disable authentication, make sure to override `allowed origins` in settings.py in production!
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:3000"  # frontend application url
    client_class = OAuth2Client

class ScreenshotViewSet(viewsets.ModelViewSet):
    queryset = Screenshot.objects.all()
    serializer_class = ScreenshotSerializers

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    # def get_queryset(self):
    #     return Screenshot.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        if not is_many:
            return super(ScreenshotViewSet, self).create(request, *args, **kwargs)
        else:
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserDetailViewSet(viewsets.ModelViewSet):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializers
    # lookup_field = [workflow_id]

    def perform_create(self, serializer):
        # with open('image.jpg', 'rb') as image_file:
        #     hash = blurhash.encode(image_file, x_components=4, y_components=3)
        #print(serializer.screenshot, "akk ss")
        # print(serializer, "akki sr")
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return UserDetail.objects.filter(user=self.request.user)
    
    # @action(methods=['get'], detail=True)
    # def share(self, request, pk):
    #     user = self.get_object()
    #     print(user, "akki user")
    #     serializer = UserDetailSerializers(data=request.data)
    #     if serializer.is_valid():
    #         return Response(serializer.data)

class ShareWorkflowListView(generics.RetrieveAPIView):
    queryset = UserDetail.objects.all().filter(share=True)
    serializer_class = UserDetailSerializers
    authentication_classes = []
    permission_classes = [AllowAny]


class UserScreenshotsListView(generics.ListAPIView):
    #queryset = UserScreenshots.objects.all()
    serializer_class = ScreenshotSerializers
    filterset_fields = ['workflow_id',]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
    def get_queryset(self):
        workflow_id =self.kwargs['workflow_id']
        return Screenshot.objects.filter(workflow_id=workflow_id)
    # def get_queryset(self):
    # workflow_id =self.kwargs['workflow_id']
    # return Screenshot.objects.filter(workflow_id=workflow_id)
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data, many=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         headers = self.get_success_headers(serializer.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED,
    #                         headers=headers)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


